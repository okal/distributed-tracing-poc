require 'test_helper'

class LookupControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get lookup_index_url
    assert_response :success
  end

end
