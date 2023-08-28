from superdesk.io.registry import register_feeding_service, register_feeding_service_parser

from . import sample

register_feeding_service(sample.SampleFeedingService)
register_feeding_service_parser(sample.SampleFeedingService.NAME, None)
