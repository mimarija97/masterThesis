import unittest

from metadata_resolver import process_topic_name
from metadata_models import basicMetadataModel,extendedMetadataModel
from metadata_harmoniser import harmonize
from metadata_processor import preprocess_metadata_into_subtrees
import time

class TestPerformance(unittest.TestCase):
    def time_harmonize_and_map(self, topic_name,preprocessed_metadata,message):
        before = time.time_ns()
        print(harmonize(process_topic_name(topic_name, preprocessed_metadata),message))
        after = time.time_ns()
        return after - before

    # todo: Test data needs to be adjusted to actually test the test cases specified. This test is not yet ready

    # tests for evaluating performance per the number of categories
    def test_performance_base_model_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_extended_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_duplicated_categories_model_extended_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    # tests to evaluate performance as the number of topic layers changes. Base case (5 levels) is tested by test_performance_base_model_base_topic_names
    def test_performance_extended_model_10_layer_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_15_layer_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_20_layer_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    # tests to evaluate performance as the number of instances changes. Base case is tested by test_performance_base_model_base_topic_names
    def test_performance_small_model_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extra_instances_base_topic_names(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    #tests on the effects of the parent child relationships on the performance

    def test_performance_basic_case_no_parents(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_extended_model_no_parents(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_m5ap("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)

    def test_performance_duplicated_categories_model_no_parents(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        performance_per_topic = [
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/living_room/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/1/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/livingroom/2/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/humidity", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/kitchen/smoke", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/ground_floor/hallway/light", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/first_floor/suite/temperature", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom2/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/firstFloor/bedroom3/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/garage/garage_door", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, ""),
            self.time_harmonize_and_map("home/garden/sittingArea/motion", preprocessed_metadata, "")]
        average = sum(performance_per_topic) / len(performance_per_topic)
        print(average)


if __name__ == '__main__':
    unittest.main()
