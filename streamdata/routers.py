from swampdragon import route_handler
from swampdragon.route_handler import BaseRouter
from .system_info import broadcast_sys_info


class TweetsRouter(BaseRouter):
	route_name = 'tweets'

	def get_subscription_channels(self, **kwargs):
		return ['tweet']

route_handler.register(TweetsRouter)