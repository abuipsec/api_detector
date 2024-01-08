# api_detector/api_detector.py

class APIDetector:
    def __init__(self):
        self.detected_apis = []

    def detect_api(self, traffic_data):
        """
        Detects API based on traffic data.

        :param traffic_data: Information extracted from network traffic.
        """
        # Placeholder: Detect API based on simple conditions
        if "api" in traffic_data.lower():
            self.detected_apis.append(traffic_data)

    def get_detected_apis(self):
        """
        Retrieves the list of detected APIs.

        :return: List of detected APIs.
        """
        return self.detected_apis
