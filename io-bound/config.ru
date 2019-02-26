# This file is used by Rack-based servers to start the application.

require_relative 'config/environment'
require 'zipkin-tracer'


zipkin_config = {
    service_name: "io-bound",
    service_port: 3000,
    sample_rate: 1,
    sampled_as_boolean: false,
    log_tracing: true,
    json_api_host: 'http://zipkin:9411/api/v1/spans'
}

use ZipkinTracer::RackHandler, zipkin_config


run Rails.application
