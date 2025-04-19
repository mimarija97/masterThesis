from metadata_harmoniser import harmonize
from metadata_resolver import process_topic_name


# preprocessing metadata
def filter_metadata(metadata, match_key):
    subtree = {}

    def dfs(current_key):
        if current_key not in metadata or current_key in subtree:
            return
        subtree[current_key] = metadata[current_key]
        for key, value in metadata.items():
            parents = value.get("has_parent")
            if isinstance(parents, list) and current_key in parents:
                dfs(key)

    dfs(match_key)
    return subtree


def preprocess_metadata_into_subtrees(metadata_dictionary):
    grouped_metadata = []
    for groupName, group in metadata_dictionary.items():
        if group["has_parent"] is not None:
            continue
        grouped_metadata.append(filter_metadata(metadata_dictionary, groupName))

    return grouped_metadata