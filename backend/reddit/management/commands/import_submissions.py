from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime

import json
import logging

from reddit.models import Submission

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Imports the submissions from the example data file'

    def handle(self, *args, **options):
        submissions = []
        with open("RS_2005-06", "r") as file:
            for line in file:
                json_data = json.loads(line)
                
                logger.info("Importing %s", json_data["title"])

                submissions.append(Submission(
                    archived=json_data["archived"],
                    author=json_data["author"],
                    created_at=make_aware(datetime.fromtimestamp(json_data["created_utc"])),
                    title=json_data["title"],
                    url=json_data["url"]
                ))

        Submission.objects.bulk_create(submissions)
