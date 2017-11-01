cluster_nodes = {
    "all_nodes": [
        "test_node"
    ],
    "cluster_nodes": [
        "test_node"
    ]
}

all_dbs = [
    "test_db"
]

db_stats = {
    "db_name": "test_db",
    "update_seq": "1-g1AAAAFLeJzLYWBg4MhgTmEQSM4vTc5ISXKA0oY5QBmmRIYk-f___2clMuBWk6QAJJPsCSpzACmLBytjxKMsAaSsnpBpeSxAkqEBSAFVzidC6QKI0v1EKD0AUXqfCKUPIEpBbs0CACPTaSc",
    "sizes": {
        "file": 38078,
        "external": 2003,
        "active": 2199
    },
    "purge_seq": 0,
    "other": {
        "data_size": 2003
    },
    "doc_del_count": 0,
    "doc_count": 1,
    "disk_size": 38078,
    "disk_format_version": 6,
    "data_size": 2199,
    "compact_running": False,
    "instance_start_time": "0"
}

node_stats = {
    "couch_replicator": {
        "changes_read_failures": {
            "value": 0,
            "type": "counter",
            "desc": "number of failed replicator changes read failures"
        },
        "changes_reader_deaths": {
            "value": 0,
            "type": "counter",
            "desc": "number of failed replicator changes readers"
        },
        "changes_manager_deaths": {
            "value": 0,
            "type": "counter",
            "desc": "number of failed replicator changes managers"
        },
        "changes_queue_deaths": {
            "value": 0,
            "type": "counter",
            "desc": "number of failed replicator changes work queues"
        },
        "checkpoints": {
            "success": {
                "value": 0,
                "type": "counter",
                "desc": "number of checkpoints successfully saves"
            },
            "failure": {
                "value": 0,
                "type": "counter",
                "desc": "number of failed checkpoint saves"
            }
        },
        "failed_starts": {
            "value": 0,
            "type": "counter",
            "desc": "number of replications that have failed to start"
        },
        "requests": {
            "value": 0,
            "type": "counter",
            "desc": "number of HTTP requests made by the replicator"
        },
        "responses": {
            "failure": {
                "value": 0,
                "type": "counter",
                "desc": "number of failed HTTP responses received by the replicator"
            },
            "success": {
                "value": 0,
                "type": "counter",
                "desc": "number of successful HTTP responses received by the replicator"
            }
        },
        "stream_responses": {
            "failure": {
                "value": 0,
                "type": "counter",
                "desc": "number of failed streaming HTTP responses received by the replicator"
            },
            "success": {
                "value": 0,
                "type": "counter",
                "desc": "number of successful streaming HTTP responses received by the replicator"
            }
        },
        "worker_deaths": {
            "value": 0,
            "type": "counter",
            "desc": "number of failed replicator workers"
        },
        "workers_started": {
            "value": 0,
            "type": "counter",
            "desc": "number of replicator workers started"
        }
    },
    "rexi": {
        "buffered": {
            "value": 0,
            "type": "counter",
            "desc": "number of rexi messages buffered"
        },
        "down": {
            "value": 3,
            "type": "counter",
            "desc": "number of rexi_DOWN messages handled"
        },
        "dropped": {
            "value": 0,
            "type": "counter",
            "desc": "number of rexi messages dropped from buffers"
        },
        "streams": {
            "timeout": {
                "init_stream": {
                    "value": 0,
                    "type": "counter",
                    "desc": "number of rexi stream initialization timeouts"
                },
                "stream": {
                    "value": 0,
                    "type": "counter",
                    "desc": "number of rexi stream timeouts"
                },
                "wait_for_ack": {
                    "value": 0,
                    "type": "counter",
                    "desc": "number of rexi stream timeouts while waiting for acks"
                }
            }
        }
    },
    "couchdb": {
        "httpd": {
            "aborted_requests": {
                "value": 0,
                "type": "counter",
                "desc": "number of aborted requests"
            },
            "bulk_docs": {
                "value": {
                    "min": 0,
                    "max": 0,
                    "arithmetic_mean": 0,
                    "geometric_mean": 0,
                    "harmonic_mean": 0,
                    "median": 0,
                    "variance": 0,
                    "standard_deviation": 0,
                    "skewness": 0,
                    "kurtosis": 0,
                    "percentile": [
                        [
                            50,
                            0
                        ],
                        [
                            75,
                            0
                        ],
                        [
                            90,
                            0
                        ],
                        [
                            95,
                            0
                        ],
                        [
                            99,
                            0
                        ],
                        [
                            999,
                            0
                        ]
                    ],
                    "histogram": [
                        [
                            0,
                            0
                        ]
                    ],
                    "n": 0
                },
                "type": "histogram",
                "desc": "distribution of the number of docs in _bulk_docs requests"
            },
            "bulk_requests": {
                "value": 0,
                "type": "counter",
                "desc": "number of bulk requests"
            },
            "requests": {
                "value": 27,
                "type": "counter",
                "desc": "number of HTTP requests"
            },
            "temporary_view_reads": {
                "value": 0,
                "type": "counter",
                "desc": "number of temporary view reads"
            },
            "view_reads": {
                "value": 0,
                "type": "counter",
                "desc": "number of view reads"
            },
            "clients_requesting_changes": {
                "value": 0,
                "type": "counter",
                "desc": "number of clients for continuous _changes"
            }
        },
        "dbinfo": {
            "value": {
                "min": 0,
                "max": 0,
                "arithmetic_mean": 0,
                "geometric_mean": 0,
                "harmonic_mean": 0,
                "median": 0,
                "variance": 0,
                "standard_deviation": 0,
                "skewness": 0,
                "kurtosis": 0,
                "percentile": [
                    [
                        50,
                        0
                    ],
                    [
                        75,
                        0
                    ],
                    [
                        90,
                        0
                    ],
                    [
                        95,
                        0
                    ],
                    [
                        99,
                        0
                    ],
                    [
                        999,
                        0
                    ]
                ],
                "histogram": [
                    [
                        0,
                        0
                    ]
                ],
                "n": 0
            },
            "type": "histogram",
            "desc": "distribution of latencies for calls to retrieve DB info"
        },
        "mrview": {
            "map_doc": {
                "value": 0,
                "type": "counter",
                "desc": "number of documents mapped in the view server"
            },
            "emits": {
                "value": 0,
                "type": "counter",
                "desc": "number of invocations of `emit' in map functions in the view server"
            }
        },
        "auth_cache_hits": {
            "value": 1,
            "type": "counter",
            "desc": "number of authentication cache hits"
        },
        "auth_cache_misses": {
            "value": 7,
            "type": "counter",
            "desc": "number of authentication cache misses"
        },
        "collect_results_time": {
            "value": {
                "min": 0,
                "max": 0,
                "arithmetic_mean": 0,
                "geometric_mean": 0,
                "harmonic_mean": 0,
                "median": 0,
                "variance": 0,
                "standard_deviation": 0,
                "skewness": 0,
                "kurtosis": 0,
                "percentile": [
                    [
                        50,
                        0
                    ],
                    [
                        75,
                        0
                    ],
                    [
                        90,
                        0
                    ],
                    [
                        95,
                        0
                    ],
                    [
                        99,
                        0
                    ],
                    [
                        999,
                        0
                    ]
                ],
                "histogram": [
                    [
                        0,
                        0
                    ]
                ],
                "n": 0
            },
            "type": "histogram",
            "desc": "microsecond latency for calls to couch_db:collect_results/3"
        },
        "database_writes": {
            "value": 11,
            "type": "counter",
            "desc": "number of times a database was changed"
        },
        "database_reads": {
            "value": 0,
            "type": "counter",
            "desc": "number of times a document was read from a database"
        },
        "db_open_time": {
            "value": {
                "min": 0,
                "max": 0,
                "arithmetic_mean": 0,
                "geometric_mean": 0,
                "harmonic_mean": 0,
                "median": 0,
                "variance": 0,
                "standard_deviation": 0,
                "skewness": 0,
                "kurtosis": 0,
                "percentile": [
                    [
                        50,
                        0
                    ],
                    [
                        75,
                        0
                    ],
                    [
                        90,
                        0
                    ],
                    [
                        95,
                        0
                    ],
                    [
                        99,
                        0
                    ],
                    [
                        999,
                        0
                    ]
                ],
                "histogram": [
                    [
                        0,
                        0
                    ]
                ],
                "n": 0
            },
            "type": "histogram",
            "desc": "milliseconds required to open a database"
        },
        "document_inserts": {
            "value": 15,
            "type": "counter",
            "desc": "number of documents inserted"
        },
        "document_writes": {
            "value": 21,
            "type": "counter",
            "desc": "number of document write operations"
        },
        "local_document_writes": {
            "value": 17,
            "type": "counter",
            "desc": "number of _local document write operations"
        },
        "httpd_request_methods": {
            "COPY": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP COPY requests"
            },
            "DELETE": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP DELETE requests"
            },
            "GET": {
                "value": 22,
                "type": "counter",
                "desc": "number of HTTP GET requests"
            },
            "HEAD": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP HEAD requests"
            },
            "OPTIONS": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP OPTIONS requests"
            },
            "POST": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP POST requests"
            },
            "PUT": {
                "value": 5,
                "type": "counter",
                "desc": "number of HTTP PUT requests"
            }
        },
        "httpd_status_codes": {
            "200": {
                "value": 22,
                "type": "counter",
                "desc": "number of HTTP 200 OK responses"
            },
            "201": {
                "value": 5,
                "type": "counter",
                "desc": "number of HTTP 201 Created responses"
            },
            "202": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 202 Accepted responses"
            },
            "204": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 204 No Content responses"
            },
            "206": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 206 Partial Content"
            },
            "301": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 301 Moved Permanently responses"
            },
            "302": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 302 Found responses"
            },
            "304": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 304 Not Modified responses"
            },
            "400": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 400 Bad Request responses"
            },
            "401": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 401 Unauthorized responses"
            },
            "403": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 403 Forbidden responses"
            },
            "404": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 404 Not Found responses"
            },
            "405": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 405 Method Not Allowed responses"
            },
            "406": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 406 Not Acceptable responses"
            },
            "409": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 409 Conflict responses"
            },
            "412": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 412 Precondition Failed responses"
            },
            "413": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 413 Request Entity Too Long responses"
            },
            "414": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 414 Request URI Too Long responses"
            },
            "415": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 415 Unsupported Media Type responses"
            },
            "416": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 416 Requested Range Not Satisfiable responses"
            },
            "417": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 417 Expectation Failed responses"
            },
            "500": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 500 Internal Server Error responses"
            },
            "501": {
                "value": 0,
                "type": "counter",
                "desc": "number of HTTP 501 Not Implemented responses"
            }
        },
        "open_databases": {
            "value": 8,
            "type": "counter",
            "desc": "number of open databases"
        },
        "open_os_files": {
            "value": 8,
            "type": "counter",
            "desc": "number of file descriptors CouchDB has open"
        },
        "request_time": {
            "value": {
                "min": 0,
                "max": 0,
                "arithmetic_mean": 0,
                "geometric_mean": 0,
                "harmonic_mean": 0,
                "median": 0,
                "variance": 0,
                "standard_deviation": 0,
                "skewness": 0,
                "kurtosis": 0,
                "percentile": [
                    [
                        50,
                        0
                    ],
                    [
                        75,
                        0
                    ],
                    [
                        90,
                        0
                    ],
                    [
                        95,
                        0
                    ],
                    [
                        99,
                        0
                    ],
                    [
                        999,
                        0
                    ]
                ],
                "histogram": [
                    [
                        0,
                        0
                    ]
                ],
                "n": 0
            },
            "type": "histogram",
            "desc": "length of a request inside CouchDB without MochiWeb"
        },
        "couch_server": {
            "lru_skip": {
                "value": 0,
                "type": "counter",
                "desc": "number of couch_server LRU operations skipped"
            }
        },
        "query_server": {
            "vdu_rejects": {
                "value": 0,
                "type": "counter",
                "desc": "number of rejections by validate_doc_update function"
            },
            "vdu_process_time": {
                "value": {
                    "min": 0,
                    "max": 0,
                    "arithmetic_mean": 0,
                    "geometric_mean": 0,
                    "harmonic_mean": 0,
                    "median": 0,
                    "variance": 0,
                    "standard_deviation": 0,
                    "skewness": 0,
                    "kurtosis": 0,
                    "percentile": [
                        [
                            50,
                            0
                        ],
                        [
                            75,
                            0
                        ],
                        [
                            90,
                            0
                        ],
                        [
                            95,
                            0
                        ],
                        [
                            99,
                            0
                        ],
                        [
                            999,
                            0
                        ]
                    ],
                    "histogram": [
                        [
                            0,
                            0
                        ]
                    ],
                    "n": 0
                },
                "type": "histogram",
                "desc": "duration of validate_doc_update function calls"
            }
        }
    },
    "couch_log": {
        "level": {
            "alert": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged alert messages"
            },
            "critical": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged critical messages"
            },
            "debug": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged debug messages"
            },
            "emergency": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged emergency messages"
            },
            "error": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged error messages"
            },
            "info": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged info messages"
            },
            "notice": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged notice messages"
            },
            "warning": {
                "value": 0,
                "type": "counter",
                "desc": "number of logged warning messages"
            }
        }
    },
    "pread": {
        "exceed_eof": {
            "value": 0,
            "type": "counter",
            "desc": "number of the attempts to read beyond end of db file"
        },
        "exceed_limit": {
            "value": 0,
            "type": "counter",
            "desc": "number of the attempts to read beyond set limit"
        }
    },
    "ddoc_cache": {
        "hit": {
            "value": 2,
            "type": "counter",
            "desc": "number of design doc cache hits"
        },
        "miss": {
            "value": 1,
            "type": "counter",
            "desc": "number of design doc cache misses"
        },
        "recovery": {
            "value": 0,
            "type": "counter",
            "desc": "number of design doc cache recoveries"
        }
    },
    "global_changes": {
        "db_writes": {
            "value": 11,
            "type": "counter",
            "desc": "number of db writes performed by global changes"
        },
        "event_doc_conflict": {
            "value": 0,
            "type": "counter",
            "desc": "number of conflicted event docs encountered by global changes"
        },
        "listener_pending_updates": {
            "value": 0,
            "type": "gauge",
            "desc": "number of global changes updates pending writes in global_changes_listener"
        },
        "rpcs": {
            "value": 7,
            "type": "counter",
            "desc": "number of rpc operations performed by global_changes"
        },
        "server_pending_updates": {
            "value": 0,
            "type": "gauge",
            "desc": "number of global changes updates pending writes in global_changes_server"
        }
    },
    "mem3": {
        "shard_cache": {
            "eviction": {
                "value": 0,
                "type": "counter",
                "desc": "number of shard cache evictions"
            },
            "hit": {
                "value": 76,
                "type": "counter",
                "desc": "number of shard cache hits"
            },
            "miss": {
                "value": 4,
                "type": "counter",
                "desc": "number of shard cache misses"
            }
        }
    },
    "fabric": {
        "worker": {
            "timeouts": {
                "value": 0,
                "type": "counter",
                "desc": "number of worker timeouts"
            }
        },
        "read_repairs": {
            "success": {
                "value": 0,
                "type": "counter",
                "desc": "number of successful read repair operations"
            },
            "failure": {
                "value": 0,
                "type": "counter",
                "desc": "number of failed read repair operations"
            }
        },
        "doc_update": {
            "errors": {
                "value": 0,
                "type": "counter",
                "desc": "number of document update errors"
            },
            "mismatched_errors": {
                "value": 0,
                "type": "counter",
                "desc": "number of document update errors with multiple error types"
            },
            "write_quorum_errors": {
                "value": 0,
                "type": "counter",
                "desc": "number of write quorum errors"
            }
        }
    }
}
