import unittest

from metadata_resolver import process_topic_name
from metadata_models import basicMetadataModel,extendedMetadataModel

class MyTestCase(unittest.TestCase):

    def test_basicModel_accuracy(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        accuracy_per_topic = []
        living_room_light=process_topic_name("home/ground_floor/living_room/light", preprocessed_metadata)
        max_matches = len(living_room_light)
        if living_room_light.get("floors") and  living_room_light["floors"]!="groundFloor":
            max_matches-=1
        if living_room_light.get("areas") and  living_room_light["areas"]!="livingroom":
            max_matches-=1
        if living_room_light.get("measurement") and  living_room_light["measurement"]!="light":
            max_matches-=1

        accuracy_per_topic.append(max_matches/3)

        living_room_section1_temp =process_topic_name("home/ground_floor/livingroom/temperature", preprocessed_metadata)
        max_matches = len(living_room_section1_temp)
        if living_room_section1_temp.get("floors") and living_room_section1_temp["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_section1_temp.get("areas") and living_room_section1_temp["areas"] != "livingroom":
            max_matches -= 1
        if living_room_section1_temp.get("measurement") and living_room_section1_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        kitchen_humidity = process_topic_name("home/ground_floor/kitchen/humidity", preprocessed_metadata)
        max_matches = len(kitchen_humidity)
        if kitchen_humidity.get("floors") and kitchen_humidity["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_humidity.get("areas") and kitchen_humidity["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_humidity.get("measurement") and kitchen_humidity["measurement"] != "humidity":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        kitchen_temp=process_topic_name("home/ground_floor/kitchen/temperature", preprocessed_metadata)
        max_matches = len(kitchen_temp)
        if kitchen_temp.get("floors") and kitchen_temp["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_temp.get("areas") and kitchen_temp["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_temp.get("measurement") and kitchen_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        kitchen_smoke=process_topic_name("home/ground_floor/kitchen/smoke", preprocessed_metadata)
        max_matches = len(kitchen_smoke)
        if kitchen_smoke.get("floors") and kitchen_smoke["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_smoke.get("areas") and kitchen_smoke["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_smoke.get("binary_measurement") and kitchen_smoke["binary_measurement"] != "smoke":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)



        hallway_light=process_topic_name("home/ground_floor/hallway/light", preprocessed_metadata)
        max_matches = len(hallway_light)
        if hallway_light.get("floors") and hallway_light["floors"] != "groundFloor":
            max_matches -= 1
        if hallway_light.get("areas") and hallway_light["areas"] != "hallway":
            max_matches -= 1
        if hallway_light.get("measurement") and hallway_light["measurement"] != "light":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        suite_temp=process_topic_name("home/first_floor/suite/temperature", preprocessed_metadata)
        max_matches = len(suite_temp)
        if suite_temp.get("floors") and suite_temp["floors"] != "firstFloor":
            max_matches -= 1
        if suite_temp.get("areas") and suite_temp["areas"] != "suite":
            max_matches -= 1
        if suite_temp.get("measurement") and suite_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        bedroom2_motion=process_topic_name("home/firstFloor/bedroom2/motion", preprocessed_metadata)
        max_matches = len(bedroom2_motion)
        if bedroom2_motion.get("floors") and bedroom2_motion["floors"] != "firstFloor":
            max_matches -= 1
        if bedroom2_motion.get("areas") and bedroom2_motion["areas"] != "bedroom2":
            max_matches -= 1
        if bedroom2_motion.get("binary_measurement") and bedroom2_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        bedroom3_motion=process_topic_name("home/firstFloor/bedroom3/motion", preprocessed_metadata)
        max_matches = len(bedroom3_motion)
        if bedroom3_motion.get("floors") and bedroom3_motion["floors"] != "firstFloor":
            max_matches -= 1
        if bedroom3_motion.get("areas") and bedroom3_motion["areas"] != "bedroom3":
            max_matches -= 1
        if bedroom3_motion.get("binary_measurement") and bedroom3_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        garage_garage_door=process_topic_name("home/garden/garage/garage_door", preprocessed_metadata)
        max_matches = len(garage_garage_door)
        if garage_garage_door.get("floors") and garage_garage_door["floors"] != "garden":
            max_matches -= 1
        if garage_garage_door.get("areas") and garage_garage_door["areas"] != "garage":
            max_matches -= 1
        if garage_garage_door.get("binary_measurement") and garage_garage_door["binary_measurement"] != "garage_door":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        sittingArea_motion=process_topic_name("home/garden/sittingArea/motion", preprocessed_metadata)

        max_matches = len(sittingArea_motion)
        if sittingArea_motion.get("floors") and sittingArea_motion["floors"] != "garden":
            max_matches -= 1
        if sittingArea_motion.get("areas") and sittingArea_motion["areas"] != "sittingArea":
            max_matches -= 1
        if sittingArea_motion.get("binary_measurement") and sittingArea_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        print(sum(accuracy_per_topic)/len(accuracy_per_topic))

    def test_basicModel_accuracy_incorrectly_named_or_missing_floor(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        accuracy_per_topic = []
        living_room_light=process_topic_name("home/ground floor/living_Room/light", preprocessed_metadata)
        max_matches = len(living_room_light)
        if living_room_light.get("floors") and  living_room_light["floors"]!="groundFloor":
            max_matches-=1
        if living_room_light.get("areas") and  living_room_light["areas"]!="livingroom":
            max_matches-=1
        if living_room_light.get("measurement") and  living_room_light["measurement"]!="light":
            max_matches-=1

        accuracy_per_topic.append(max_matches/3)

        suite_temp=process_topic_name("home/first_floors/suite/temperature", preprocessed_metadata)
        max_matches = len(suite_temp)
        if suite_temp.get("floors") and suite_temp["floors"] != "firstFloor":
            max_matches -= 1
        if suite_temp.get("areas") and suite_temp["areas"] != "suite":
            max_matches -= 1
        if suite_temp.get("measurement") and suite_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        bedroom2_motion=process_topic_name("home/first   Floor/bedroom2/motion", preprocessed_metadata)
        max_matches = len(bedroom2_motion)
        if bedroom2_motion.get("floors") and bedroom2_motion["floors"] != "firstFloor":
            max_matches -= 1
        if bedroom2_motion.get("areas") and bedroom2_motion["areas"] != "bedroom2":
            max_matches -= 1
        if bedroom2_motion.get("binary_measurement") and bedroom2_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        garage_garage_door=process_topic_name("home/garage/garage_door", preprocessed_metadata)
        max_matches = len(garage_garage_door)
        if garage_garage_door.get("floors") and garage_garage_door["floors"] != "garden":
            max_matches -= 1
        if garage_garage_door.get("areas") and garage_garage_door["areas"] != "garage":
            max_matches -= 1
        if garage_garage_door.get("binary_measurement") and garage_garage_door["binary_measurement"] != "garage_door":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        sittingArea_motion=process_topic_name("home/sittingArea/motion", preprocessed_metadata)

        max_matches = len(sittingArea_motion)
        if sittingArea_motion.get("floors") and sittingArea_motion["floors"] != "garden":
            max_matches -= 1
        if sittingArea_motion.get("areas") and sittingArea_motion["areas"] != "sittingArea":
            max_matches -= 1
        if sittingArea_motion.get("binary_measurement") and sittingArea_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        print(sum(accuracy_per_topic)/len(accuracy_per_topic))

    def test_basicModel_accuracy_incorrectly_named_area(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        accuracy_per_topic = []
        living_room_light=process_topic_name("home/ground_floor/living Room/light", preprocessed_metadata)
        max_matches = len(living_room_light)
        if living_room_light.get("floors") and  living_room_light["floors"]!="groundFloor":
            max_matches-=1
        if living_room_light.get("areas") and  living_room_light["areas"]!="livingroom":
            max_matches-=1
        if living_room_light.get("measurement") and  living_room_light["measurement"]!="light":
            max_matches-=1

        accuracy_per_topic.append(max_matches/3)

        living_room_section1_temp =process_topic_name("home/ground_floor/living room/temperature", preprocessed_metadata)
        max_matches = len(living_room_section1_temp)
        if living_room_section1_temp.get("floors") and living_room_section1_temp["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_section1_temp.get("areas") and living_room_section1_temp["areas"] != "livingroom":
            max_matches -= 1
        if living_room_section1_temp.get("measurement") and living_room_section1_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        kitchen_humidity = process_topic_name("home/ground_floor/kitchens/humidity", preprocessed_metadata)
        max_matches = len(kitchen_humidity)
        if kitchen_humidity.get("floors") and kitchen_humidity["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_humidity.get("areas") and kitchen_humidity["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_humidity.get("measurement") and kitchen_humidity["measurement"] != "humidity":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)



        kitchen_smoke=process_topic_name("home/ground_floor/smoke", preprocessed_metadata)
        max_matches = len(kitchen_smoke)
        if kitchen_smoke.get("floors") and kitchen_smoke["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_smoke.get("binary_measurement") and kitchen_smoke["binary_measurement"] != "smoke":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 2)

        print(sum(accuracy_per_topic)/len(accuracy_per_topic))

    def test_basicModel_accuracy_incorrectly_named_leaf(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        accuracy_per_topic = []
        living_room_light=process_topic_name("home/ground_floor/living_room/co2", preprocessed_metadata)
        max_matches = len(living_room_light)
        if living_room_light.get("floors") and  living_room_light["floors"]!="groundFloor":
            max_matches-=1
        if living_room_light.get("areas") and  living_room_light["areas"]!="livingroom":
            max_matches-=1
        if living_room_light.get("measurement") and  living_room_light["measurement"]!="light":
            max_matches-=1

        accuracy_per_topic.append(max_matches/3)

        living_room_section1_temp =process_topic_name("home/ground_floor/living_room/temperatur", preprocessed_metadata)
        max_matches = len(living_room_section1_temp)
        if living_room_section1_temp.get("floors") and living_room_section1_temp["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_section1_temp.get("areas") and living_room_section1_temp["areas"] != "livingroom":
            max_matches -= 1
        if living_room_section1_temp.get("measurement") and living_room_section1_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)
        # living_room_section2_temp =process_topic_name("home/ground_floor/livingroom/temperature", preprocessed_metadata)
        # max_matches = len(living_room_section2_temp)
        # if living_room_section2_temp.get("floors") and living_room_section2_temp["floors"] != "groundFloor":
        #     max_matches -= 1
        # if living_room_section2_temp.get("areas") and living_room_section2_temp["floors"] != "livingroom":
        #     max_matches -= 1
        # if living_room_section2_temp.get("measurement") and living_room_section2_temp["measurement"] != "temperature":
        #     max_matches -= 1
        #
        # accuracy_per_topic.append(max_matches / 3)

        kitchen_humidity = process_topic_name("home/ground_floor/kitchen/energy", preprocessed_metadata)
        max_matches = len(kitchen_humidity)
        if kitchen_humidity.get("floors") and kitchen_humidity["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_humidity.get("areas") and kitchen_humidity["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_humidity.get("measurement") and kitchen_humidity["measurement"] != "humidity":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        kitchen_temp=process_topic_name("home/ground_floor/kitchen/temperatur", preprocessed_metadata)
        max_matches = len(kitchen_temp)
        if kitchen_temp.get("floors") and kitchen_temp["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_temp.get("areas") and kitchen_temp["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_temp.get("measurement") and kitchen_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        kitchen_smoke=process_topic_name("home/ground_floor/kitchen", preprocessed_metadata)
        max_matches = len(kitchen_smoke)
        if kitchen_smoke.get("floors") and kitchen_smoke["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_smoke.get("areas") and kitchen_smoke["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_smoke.get("binary_measurement") and kitchen_smoke["binary_measurement"] != "smoke":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        print(sum(accuracy_per_topic)/len(accuracy_per_topic))


    def test_incompleteModel_accuracy(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(extendedMetadataModel)
        accuracy_per_topic = []
        living_room_light = process_topic_name("home/ground_floor/living_room/light", preprocessed_metadata)
        max_matches = len(living_room_light)
        if living_room_light.get("floors") and living_room_light["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_light.get("areas") and living_room_light["areas"] != "livingroom":
            max_matches -= 1
        if living_room_light.get("measurement") and living_room_light["measurement"] != "light":
            max_matches -= 1

        accuracy_per_topic.append(max_matches / 3)

        living_room_section1_temp = process_topic_name("home/ground_floor/living_room/tempDevice1/temperature",
                                                       preprocessed_metadata)
        max_matches = len(living_room_section1_temp)
        if living_room_section1_temp.get("floors") and living_room_section1_temp["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_section1_temp.get("areas") and living_room_section1_temp["areas"] != "livingroom":
            max_matches -= 1
        if living_room_section1_temp.get("device") and living_room_section1_temp[
            "device"] != "tempDevice1":
            max_matches -= 1
        if living_room_section1_temp.get("measurement") and living_room_section1_temp[
            "measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 4)

        print(sum(accuracy_per_topic)/len(accuracy_per_topic))


    def test_unplanned_content_in_topic_name(self):
        preprocessed_metadata = preprocess_metadata_into_subtrees(basicMetadataModel)
        accuracy_per_topic = []
        living_room_light = process_topic_name("home/floors/ground_floor/areas/living_room/measurement/light", preprocessed_metadata)
        max_matches = len(living_room_light)
        if living_room_light.get("floors") and living_room_light["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_light.get("areas") and living_room_light["areas"] != "livingroom":
            max_matches -= 1
        if living_room_light.get("measurement") and living_room_light["measurement"] != "light":
            max_matches -= 1

        accuracy_per_topic.append(max_matches / 3)

        living_room_section1_temp = process_topic_name("home/floors/ground_floor/areas/livingroom/measurement/temperature",
                                                       preprocessed_metadata)
        max_matches = len(living_room_section1_temp)
        if living_room_section1_temp.get("floors") and living_room_section1_temp["floors"] != "groundFloor":
            max_matches -= 1
        if living_room_section1_temp.get("areas") and living_room_section1_temp["areas"] != "livingroom":
            max_matches -= 1
        if living_room_section1_temp.get("measurement") and living_room_section1_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)


        kitchen_humidity = process_topic_name("home/floors/ground_floor/areas/kitchen/measurement/humidity", preprocessed_metadata)
        max_matches = len(kitchen_humidity)
        if kitchen_humidity.get("floors") and kitchen_humidity["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_humidity.get("areas") and kitchen_humidity["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_humidity.get("measurement") and kitchen_humidity["measurement"] != "humidity":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        kitchen_temp = process_topic_name("home/floors/ground_floor/areas/kitchen/measurement/temperature", preprocessed_metadata)
        max_matches = len(kitchen_temp)
        if kitchen_temp.get("floors") and kitchen_temp["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_temp.get("areas") and kitchen_temp["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_temp.get("measurement") and kitchen_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        kitchen_smoke = process_topic_name("home/floors/ground_floor/areas/kitchen/binary_measurement/smoke", preprocessed_metadata)
        max_matches = len(kitchen_smoke)
        if kitchen_smoke.get("floors") and kitchen_smoke["floors"] != "groundFloor":
            max_matches -= 1
        if kitchen_smoke.get("areas") and kitchen_smoke["areas"] != "kitchen":
            max_matches -= 1
        if kitchen_smoke.get("binary_measurement") and kitchen_smoke["binary_measurement"] != "smoke":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        hallway_light = process_topic_name("home/floors/ground_floor/areas/hallway/measurement/light", preprocessed_metadata)
        max_matches = len(hallway_light)
        if hallway_light.get("floors") and hallway_light["floors"] != "groundFloor":
            max_matches -= 1
        if hallway_light.get("areas") and hallway_light["areas"] != "hallway":
            max_matches -= 1
        if hallway_light.get("measurement") and hallway_light["measurement"] != "light":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        suite_temp = process_topic_name("home/floors/first_floor/areas/suite/measurement/temperature", preprocessed_metadata)
        max_matches = len(suite_temp)
        if suite_temp.get("floors") and suite_temp["floors"] != "firstFloor":
            max_matches -= 1
        if suite_temp.get("areas") and suite_temp["areas"] != "suite":
            max_matches -= 1
        if suite_temp.get("measurement") and suite_temp["measurement"] != "temperature":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        bedroom2_motion = process_topic_name("home/floors/firstFloor/areas/bedroom2/binary_measurement/motion", preprocessed_metadata)
        max_matches = len(bedroom2_motion)
        if bedroom2_motion.get("floors") and bedroom2_motion["floors"] != "firstFloor":
            max_matches -= 1
        if bedroom2_motion.get("areas") and bedroom2_motion["areas"] != "bedroom2":
            max_matches -= 1
        if bedroom2_motion.get("binary_measurement") and bedroom2_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        bedroom3_motion = process_topic_name("home/floors/firstFloor/areas/bedroom3/binary_measurement/motion", preprocessed_metadata)
        max_matches = len(bedroom3_motion)
        if bedroom3_motion.get("floors") and bedroom3_motion["floors"] != "firstFloor":
            max_matches -= 1
        if bedroom3_motion.get("areas") and bedroom3_motion["areas"] != "bedroom3":
            max_matches -= 1
        if bedroom3_motion.get("binary_measurement") and bedroom3_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        garage_garage_door = process_topic_name("home/floors/garden/areas/garage/binary_measurement/garage_door", preprocessed_metadata)
        max_matches = len(garage_garage_door)
        if garage_garage_door.get("floors") and garage_garage_door["floors"] != "garden":
            max_matches -= 1
        if garage_garage_door.get("areas") and garage_garage_door["areas"] != "garage":
            max_matches -= 1
        if garage_garage_door.get("binary_measurement") and garage_garage_door["binary_measurement"] != "garage_door":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        sittingArea_motion = process_topic_name("home/floors/garden/areas/sittingArea/binary_measurement/motion", preprocessed_metadata)

        max_matches = len(sittingArea_motion)
        if sittingArea_motion.get("floors") and sittingArea_motion["floors"] != "garden":
            max_matches -= 1
        if sittingArea_motion.get("areas") and sittingArea_motion["areas"] != "sittingArea":
            max_matches -= 1
        if sittingArea_motion.get("binary_measurement") and sittingArea_motion["binary_measurement"] != "motion":
            max_matches -= 1
        accuracy_per_topic.append(max_matches / 3)

        print(sum(accuracy_per_topic) / len(accuracy_per_topic))
        # add assertion here



if __name__ == '__main__':
    unittest.main()
