from helpers.Base import BaseResource

class HealthResource(BaseResource):

    def get(self):
        return {
            "Health" : "Site is Working"
        }