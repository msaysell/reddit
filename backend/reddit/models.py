from django.db import models

# Create your models here.
class Submission(models.Model):
    archived = models.BooleanField()
    author = models.CharField(max_length=256)
    created_at = models.DateTimeField()
    title = models.CharField(max_length=512)
    url = models.CharField(max_length=512)

    """
    {
        "domain":"downingstreetmemo.com",
        "edited":false,
        "gilded":6,
        "hidden":false,
        "hide_score":false,
        "id":"87",
        "is_crosspostable":true,
        "is_reddit_media_domain":false,
        "is_self":false,"is_video":false,
        "link_flair_css_class":null,
        "link_flair_richtext":[],
        "link_flair_text":null,
        "link_flair_text_color":"dark",
        "link_flair_type":"text",
        "locked":false,
        "media":null,
        "media_embed":{},
        "no_follow":false,
        "num_comments":390,
        "num_crossposts":0,
        "over_18":false,
        "parent_whitelist_status":"all_ads",
        "permalink":"\/r\/reddit.com\/comments\/87\/the_downing_street_memo\/",
        "rte_mode":"markdown",
        "score":183,
        "secure_media":null,
        "secure_media_embed":{},
        "selftext":"",
        "send_replies":true,
        "spoiler":false,
        "stickied":false,
        "subreddit":"reddit.com",
        "subreddit_id":"t5_6",
        "subreddit_name_prefixed":"r\/reddit.com",
        "subreddit_type":"archived",
        "suggested_sort":null,
        "thumbnail":"default",
        "thumbnail_height":null,
        "thumbnail_width":null,
        "title":"The Downing Street Memo",
        "url":"http:\/\/www.downingstreetmemo.com",
        "whitelist_status":"all_ads"
    }
    """