from common.models.entity import ApiEvent


class Test_ApiEvent:
    def test_options_event_sets_flag(self):
        test_event = {"httpMethod": "OPTIONS"}

        result = ApiEvent(test_event)

        assert result.IS_OPTIONS

    def test_get_method_sets_flag(self):
        test_event = {"httpMethod": "GET"}

        result = ApiEvent(test_event)

        assert result.IS_GET

    def test_post_method_sets_flag(self):
        test_event = {"httpMethod": "POST"}

        result = ApiEvent(test_event)

        assert result.IS_POST

    def test_proxy_path_is_extracted_if_found(self):
        test_path = "A/Test/Path"
        test_event = {"pathParameters": {"proxy": test_path}}

        result = ApiEvent(test_event)

        assert result.path == test_path

    def test_proxy_path_is_split_on_forward_slash(self):
        test_path = "A/Test/Path"
        test_event = {"pathParameters": {"proxy": test_path}}

        result = ApiEvent(test_event)

        assert result.path_parts == test_path.split("/")
