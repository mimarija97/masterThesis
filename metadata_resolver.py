"""Utility class which matches data in a string to a predefined dictionary of metadata.

Test me.
"""
import copy

METADATA_CACHE = {}


# match instances of the metadata category to the topic level
def match_metadata_category(topic_level, metadata_category_key, metadata_category_value):
    result = {}
    instance_match = None

    for instance_name, instance in metadata_category_value.items():
        # these need to be ignored
        if instance_name in ("has_parent", "single"):
            continue
        # if the input string matches the metadata instance name or the aliases if they exist return the instance name
        if topic_level == instance_name or (
                instance is not None and instance["aliases"] is not None and topic_level in instance["aliases"]):
            instance_match = instance_name
            break

    if instance_match is not None:
        result.update({metadata_category_key: instance_match})

    return result


# update the result such that: if the matched key is already in the result and the metadata category has single=true overwrite the value
# otherwise add to list of values
def update_map(result, matched_categories, metadata_dictionary):
    for key, value in matched_categories.items():
        single = True
        if key in metadata_dictionary:
            single = metadata_dictionary[key]["single"]

        if single:
            result[key] = value
        elif key in result:
            # Ensure result[key] is a set for uniqueness
            # if not value:
            #     val=[]
            # elif not isinstance(value, list):
            #     val=[value]
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = list(set([result[key]] + [value]))
        else:
            result[key] = value


def clear_metadata_category_from_dictionary(key, single, metadata_dictionary):
    """Clear the already processed metadata from the metadata dictionary so that it is not processed with the next layer of the topic name."""
    if single:
        for child_key, child_value in metadata_dictionary.items():
            if child_key == key or child_value["has_parent"] is None:
                continue
            child_value["has_parent"] = [item for item in child_value["has_parent"] if item != key]
            if child_value["has_parent"] == []:
                child_value["has_parent"] = None
        metadata_dictionary.pop(key, None)


# in case parents are processed filter out all which are not linked in the parents.
def cleanup_current_group(key, value, result, complete_metadata_dictionary):
    # if nothing was found until now, no parent or none of the parents in the result then return without doing any changes
    if result is None or complete_metadata_dictionary[key]["has_parent"] is None or not any(
            p in result for p in complete_metadata_dictionary[key]["has_parent"]):
        return
    # for each parent in has_parent, fetch the values that are allowed and filter by all of them in the end
    allowed_keys = []
    for parent in complete_metadata_dictionary[key]["has_parent"]:
        if (parent in result):
            if key not in complete_metadata_dictionary[parent][result[parent]]:
                continue
            allowed_keys.append(
                complete_metadata_dictionary[parent][result[parent]][key])

    # Allowed keys for children but removes them from the main dictionary
    value = {
        k: v
        for k, v in value.items()
        if (k in allowed_keys or k in ("has_parent", "single"))
    }


# original_metadata_dictionary is the subtree which was created in the caller method
def match_metadata(topic_name, original_metadata_dictionary):
    metadata_result = {}
    # copy the subtree so comparisons can be done later on the parents.
    metadata_dictionary = copy.deepcopy(original_metadata_dictionary)

    # returns the metadata class which has parent null. Once the parent class is removed from the tree after it is processed
    # the name is removed from the hasParent so that the kid class now has has_parent=None
    def get_root_categories():
        parent = {
            k: v for k, v in original_metadata_dictionary.items() if
            (k in metadata_dictionary and (metadata_dictionary[k].get("has_parent") is None or any(p in metadata_result for p in v.get("has_parent"))))
        }
        if parent:
            return parent
        else:
            return metadata_dictionary

    topic_parts = topic_name.split("/")
    for part in topic_parts:
        # Fetch categories where "has_parent" is None. In case the root category is processed its children become
        # the new root categories(unless they are children of multiple classes)
        root_metadata_categories = get_root_categories()
        # for each of the root categories
        for parent_key, parent_value in root_metadata_categories.items():
            # cleanup the instances, to only contain the relevant instances of the category
            cleanup_current_group(parent_key, parent_value, metadata_result, original_metadata_dictionary)
            # match the topic part to the root_metadata_categories item
            match_group = match_metadata_category(part, parent_key, parent_value)
            if match_group:  # if match group is not none or empty
                # update metadata_result such that matches from the match_group are added to metadata_result
                update_map(metadata_result, match_group, root_metadata_categories)
                # remove "paret_key" from the metadata dictionary. Updates children with parent null
                clear_metadata_category_from_dictionary(parent_key, parent_value["single"], metadata_dictionary)
                # filter the child that have the parent_key as parent
    return metadata_result


# this is the main method which starts the calculation
def process_topic_name(topic_name, metadata_dictionary):
    # must do a deep copy so it doesn't change the stored metadata model
    local_metadata_copy = copy.deepcopy(metadata_dictionary)
    # check if the topic name is in the cache. Simple key value, according to python O(0), rarely(worst-case) in case of many collisions O(n)
    if topic_name in METADATA_CACHE:
        return METADATA_CACHE[topic_name]
    # holder for the result
    return_metadata = {}

    for sub_dictionary in local_metadata_copy:
        # for each category which does not have a parent or all parents are in the subdictionary remove from the local_metadata copy
        # this is done before the data in the subdictionary is changed in update_map. This is so that categories which are only relevant for this
        # metadata structure are not processed again.
        update_map(
            return_metadata, match_metadata(topic_name, sub_dictionary), sub_dictionary)

    METADATA_CACHE[topic_name] = return_metadata

    return return_metadata

