import unittest

from metadata_resolver import process_topic_name
from metadata_models import basicMetadataModel, extendedMetadataModel, binary_yes, binary_no, temperature_raw, \
    temperature_json, humidity_json, extendedMetadataModelDuplicated, basicMetadataModelNoParents, \
    extendedMetadataModelNoParents, extendedMetadataModelDuplicatedNoParents, limitedMetadataModelWithParentLinks, \
    largeMetadataModelWithParentLinks
from metadata_harmoniser import harmonize
from metadata_processor import preprocess_metadata_into_subtrees
import time


class TestPerformance(unittest.TestCase):
    def time_harmonize_and_map(self, topic_name, preprocessed_metadata, message):
        before = time.time_ns()
        print(harmonize(process_topic_name(topic_name, preprocessed_metadata), message))
        after = time.time_ns()
        return after - before

    # tests for evaluating performance per the number of categories
    def test_performance_base_model_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average / 1000000)

    def test_performance_extended_model_extended_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/lightDevice1/light", preprocessed_metadata,
                                        binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/lightDevice1/light", preprocessed_metadata,
                                        binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/section1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/section2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidityDevice1/humidity", preprocessed_metadata,
                                        humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/tempDevice2/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/lightDevice1/light", preprocessed_metadata,
                                        binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motionSensor1/motion", preprocessed_metadata,
                                        binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motionSensor2/motion", preprocessed_metadata,
                                        binary_no),
            self.time_harmonize_and_map("home/garden/garage/garageContactSensor1/garage_door", preprocessed_metadata,
                                        binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_duplicated_categories_model_extended_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModelDuplicated)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    # tests to evaluate performance as the number of topic layers changes. Base case (5 levels) is tested by test_performance_base_model_base_topic_names
    def test_performance_extended_model_10_layer_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion/tuwien/ac/at/master/thesis",
                                        preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_15_layer_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map(
                "home/ground_floor/living_room/light/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map(
                "home/ground_floor/living_room/light/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/ground_floor/livingroom/1/temperature/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map(
                "home/ground_floor/livingroom/2/temperature/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_json),
            self.time_harmonize_and_map(
                "home/ground_floor/kitchen/humidity/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map(
                "home/ground_floor/kitchen/temperature/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map(
                "home/ground_floor/kitchen/smoke/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/ground_floor/hallway/light/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/first_floor/suite/temperature/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map(
                "home/firstFloor/bedroom2/motion/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map(
                "home/firstFloor/bedroom3/motion/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/garden/garage/garage_door/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map(
                "home/garden/sittingArea/motion/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/garden/sittingArea/motion/tuwien/ac/at/master/thesis/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_20_layer_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map(
                "home/ground_floor/living_room/light/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map(
                "home/ground_floor/living_room/light/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/ground_floor/livingroom/1/temperature/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map(
                "home/ground_floor/livingroom/2/temperature/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_json),
            self.time_harmonize_and_map(
                "home/ground_floor/kitchen/humidity/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map(
                "home/ground_floor/kitchen/temperature/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map(
                "home/ground_floor/kitchen/smoke/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/ground_floor/hallway/light/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/first_floor/suite/temperature/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map(
                "home/firstFloor/bedroom2/motion/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map(
                "home/firstFloor/bedroom3/motion/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/garden/garage/garage_door/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map(
                "home/garden/sittingArea/motion/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_no),
            self.time_harmonize_and_map(
                "home/garden/sittingArea/motion/security/energy/binary/automations/health/security/energy/binary/automations/health",
                preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    # tests to evaluate performance as the number of instances changes. Base case is tested by test_performance_base_model_base_topic_names
    def test_performance_small_model_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(limitedMetadataModelWithParentLinks)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extra_instances_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(largeMetadataModelWithParentLinks)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    # tests on the effects of the parent child relationships on the performance

    def test_performance_basic_case_no_parents(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModelNoParents)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_no_parents(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModelNoParents)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_duplicated_categories_model_no_parents(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModelDuplicatedNoParents)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata,
                                        temperature_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, humidity_json),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata,
                                        temperature_raw),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, temperature_raw),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, binary_yes),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_no),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, binary_yes)]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)


if __name__ == '__main__':
    unittest.main()
