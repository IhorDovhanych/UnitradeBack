INDICES_FOR_MAPPING = {
    "roles": {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
            "id": {"type": "integer"},
            "name": {
                "type": "text",
                "fields": {
                "keyword": {
                    "type": "keyword"
                }
                }
            }
            }
        }
    },
    "users": {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
                "id": {"type": "integer"},
                "name": {
                    "type": "text",
                    "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                    }
                },
                "email": {"type": "text"},
                "role_id": {"type": "integer"},
                "picture": {"type": "text"},
                "created_at": {"type": "date"},
                "updated_at": {"type": "date"}
            }
        }
    },
    "posts": {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
            "id": {"type": "integer"},
            "title": {
                "type": "text",
                "fields": {
                "keyword": {
                    "type": "keyword"
                }
                }
            },
            "description": {"type": "text"},
            "display": {"type": "boolean"},
            "price": {"type": "float"},
            "user_id": {"type": "integer"},
            "created_at": {"type": "date"},
            "updated_at": {"type": "date"}
            }
        }
    },
    "categories":{
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
            "id": {"type": "integer"},
            "name": {
                "type": "text",
                "fields": {
                "keyword": {
                    "type": "keyword"
                }
                }
            },
            "post_id": {"type": "integer"}
            }
        }
    },
    "images": {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
            "id": {"type": "integer"},
            "url": {"type": "text"},
            "post_id": {"type": "integer"}
            }
        }
    },
    "reports": {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        "mappings": {
            "properties": {
            "id": {"type": "integer"},
            "title": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword"
                    }
                }
            },
            "description": {"type": "text"},
            "user_id": {"type": "integer"},
            "post_id": {"type": "integer"},
            "created_at": {"type": "date"},
            "updated_at": {"type": "date"}
            }
        }
    }
}