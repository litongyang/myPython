#!/bin/sh

ip="10.10.202.112"
index="crm_v2"

curl -XDELETE http://${ip}:9200/${index}
curl -XPOST http://${ip}:9200/${index}
curl -XPOST http://${ip}:9200/${index}/crm/_mapping?ignore_conflicts=true -d '
 {
     "crm": {
         "properties": {
             "is_permanent": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "level_level": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "register_date_t": {
                 "format": "yyyy-MM-dd",
                 "type": "date"
             },
             "last_logindate_t": {
                 "format": "yyyy-MM-dd",
                 "type": "date"
             },
             "city": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "last_logindate": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "points_expired_time": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "upgrade_points": {
                 "type": "integer"
             },
             "register_date": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "referral_id": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "age": {
                 "type": "integer"
             },
             "name": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "province": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "gender": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "user_id": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "is_trusteeship": {
                 "type": "integer"
             },
             "trusteeship_date": {
                 "format": "yyyy-MM-dd",
                 "type": "date"
             },
             "channel": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "trusteeship_time": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "is_bind_card": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "bind_card_time": {
                 "index": "not_analyzed",
                 "type": "string"
             },
              "bind_card_time_t": {
                 "index": "not_analyzed",
                 "type": "date",
                 "format":"yyyy-MM-dd"
             },
              "bind_card_category": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "fund": {
                 "properties": {
                     "new_user_submit_time_int": {
                         "type": "integer"
                     },
                     "avg_amount": {
                         "type": "integer"
                     },
                     "first_time_int": {
                         "type": "integer"
                     },
                     "brushstroke_amount_max": {
                         "type": "integer"
                     },
                     "new_user_amount": {
                         "type": "integer"
                     },
                     "all_amount": {
                         "type": "long"
                     },
                     "new_user_submit_time": {
                         "format": "yyyy-MM-dd",
                         "type": "date"
                     },
                     "brushstroke_amount_min": {
                         "type": "integer"
                     },
                     "is_new_user": {
                         "type": "integer"
                     },
                     "first_time": {
                         "format": "yyyy-MM-dd",
                         "type": "date"
                     },
                     "all_count": {
                         "type": "integer"
                     },
                     "lastest_time": {
                         "format": "yyyy-MM-dd",
                         "type": "date"
                     },
                     "no_new_user_amount": {
                         "type": "integer"
                     },									 
					 "no_debt_swap_cnt": {
                         "type": "integer"
                     },
					 "debt_swap_cnt": {
                         "type": "integer"
                     },
					 "no_debt_swap_amount": {
                         "type": "integer"
                     },
					 "debt_swap_amount": {
                         "type": "integer"
                     },
					 "first_time_invest_amount": {
                         "type": "double"
                     },
					 "no_new_user_amount": {
                         "type": "integer"
                     },
					 "pc_invest_cnt": {
                         "type": "integer"
                     },
					 "app_invest_cnt": {
                         "type": "integer"
                     },
					 "h5_invest_cnt": {
                         "type": "integer"
                     },
					 "other_channel_cnt": {
                         "type": "integer"
                     },
                     "no_debtSwap_newUser_cnt": {
                         "type": "integer"
                     },
					 "no_debtSwap_newUser_cnt_ratio": {
                         "type": "double"
                     },
					 "no_debt_swap_cnt_ratio": {
                         "type": "double"
                     },
					 "debt_swap_cnt_ratio": {
                         "type": "double"
                     },
					 "no_debt_swap_amount_ratio": {
                         "type": "double"
                     },
					 "debt_swap_amount_ratio": {
                         "type": "double"
                     },
					 "new_amount_ratio": {
                         "type": "double"
                     },
					 "pc_invest_cnt_ratio": {
                         "type": "double"
                     },
					 "app_invest_cnt_ratio": {
                         "type": "double"
                     },
					 "h5_invest_cnt_ratio": {
                         "type": "double"
                     },
                     "first_invest_type": {
                         "type": "string"
                     },
                     "first_invest_type_int": {
                         "type": "integer"
                     },
                     "first_no_debt_days": {
                         "type": "integer"
                     },
                     "first_debt_days": {
                         "type": "integer"
                     },
                     "first_new_days": {
                         "type": "integer"
                     },
                     "first_no_debt_title": {
                        "index": "not_analyzed",
                         "type": "string"
                     },
                     "first_debt_title": {
                        "index": "not_analyzed",
                         "type": "string"
                     },
                     "first_new_title": {
                        "index": "not_analyzed",
                         "type": "string"
                     },
                     "last_no_debt_amount": {
                         "type": "double"
                     },
                     "last_debt_amount": {
                         "type": "double"
                     },
                     "last_new_amount": {
                         "type": "double"
                     },
                     "logger": {
						"type":"nested",
                         "properties": {
                             "due_date_int": {
                                 "type": "integer"
                             },
                             "amount": {
                                 "type": "integer"
                             },
                             "category": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
                             "due_amount": {
                                 "type": "double"
                             },
                             "due_date": {
                                 "format": "yyyy-MM-dd",
                                 "type": "date"
                             },
                             "submit_time_int": {
                                 "type": "integer"
                             },
                             "submit_time": {
                                 "format": "yyyy-MM-dd",
                                 "type": "date"
                             },
                             "invest_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             }
                         }
                     },
                     "lastest_time_int": {
                         "type": "integer"
                     }
                 }
             },
             "total_points": {
                 "type": "integer"
             },
             "coupon": {
                 "properties": {
                     "rebate_used": {
                         "type": "integer"
                     },
                     "points_count": {
                         "type": "long"
                     },
                     "turnplate_count": {
                         "type": "long"
                     },
                     "send": {
                         "type": "long"
                     },
                     "send_user_id": {
                         "type": "string"
                     },
                     "avg_amount": {
                         "type": "long"
                     },
                     "register_used": {
                         "type": "integer"
                     },
                     "accept": {
                         "type": "long"
                     },
                     "weekend_used": {
                         "type": "integer"
                     },
                     "weekend_unused": {
                         "type": "integer"
                     },
                     "all_amount": {
                         "type": "integer"
                     },
                     "turnplate_used": {
                         "type": "integer"
                     },
                     "newyear_unused": {
                         "type": "integer"
                     },
                     "all_use_count": {
                         "type": "integer"
                     },
                     "rebate_count": {
                         "type": "long"
                     },
                     "all_count": {
                         "type": "integer"
                     },
                     "weekend_count": {
                         "type": "long"
                     },
                     "logger": {
			"type":"nested",
                         "properties": {
                             "amount": {
                                 "type": "integer"
                             },
                             "tag": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
                             "coupon_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
                             "is_used": {
                              "type": "integer"
                            },
                             "created_time_int": {
                                 "type": "long"
                             },
                             "submit_time_int": {
                                 "type": "long"
                             },
                             "coupon_name": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
                             "created_time": {
                                 "format": "yyyy-MM-dd",
                                 "type": "date"
                             },
                             "submit_time": {
                                 "format": "yyyy-MM-dd",
                                 "type": "date"
                             },
                             "invest_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             }
                         }
                     },
                     "newyear_count": {
                         "type": "long"
                     },
                     "points_unused": {
                         "type": "integer"
                     },
                     "rebate_unused": {
                         "type": "integer"
                     },
                     "turnplate_unused": {
                         "type": "integer"
                     },
                     "points_used": {
                         "type": "integer"
                     },
                     "register_unused": {
                         "type": "integer"
                     },
                     "register_count": {
                         "type": "long"
                     },
                     "accept_user_id": {
                         "type": "string"
                     },
                     "last_new_coupon_endtime": {
                         "type": "string"
                     },
                     "newyear_used": {
                         "type": "integer"
                     }
                 }
             },
             "activity": {
                 "properties": {
                     "activity_type": {
                         "type": "integer"
                     },
					 "type_cnt": {
                         "type": "integer"
                     },
                     "type_amount": {
                        "type": "double"
                     },
                     "logger": {
						"type":"nested",
                         "properties": {
                             "activity_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "activity_type": {
                                 "index": "not_analyzed",
                                 "type": "integer"
                             },
							 "activity_name": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "award_type": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "type_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "type_name": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "correspond_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "amount": {
                                 "index": "not_analyzed",
                                 "type": "double"
                             },
							 "correspond_investment": {
                                 "index": "not_analyzed",
                                 "type": "double"
                             },
							  "send_time": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							  "is_send_status": {
                                 "index": "not_analyzed",
                                 "type": "integer"
                             },
							  "is_joined": {
                                 "index": "not_analyzed",
                                 "type": "integer"
                             }, 
							 "created_user_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "modified_user_id": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "date_entered": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "date_modified": {
                                 "index": "not_analyzed",
                                 "type": "string"
                             },
							 "deleted": {
                                 "index": "not_analyzed",
                                 "type": "integer"
                             }
                         }
                     }
                 }
             },
             "fund_account": {
                 "properties": {
                    "balance_amount":{
                        "type": "double"
                    },
                    "total_amount":{
                        "type": "double"
                    },
                    "available_amount":{
                        "type": "double"
                    },
                    "first_deposit_date":{
                        "type": "string"
                    },
                    "first_withdraw_date":{
                        "type": "string"
                    },
                    "last_withdraw_date":{
                        "type": "string"
                    },
                    "logger":{
                        "type":"nested",
                         "properties": {
                             "type_amount": {
							  "index": "not_analyzed",
                              "type": "string"
                            },
                             "type_name": {
							  "index": "not_analyzed",
                              "type": "string"
                            },
                             "amount": {
                              "type": "double"
                            },
                             "amount_date": {
                              "format": "yyyy-MM-dd",
                              "type": "date"
                            }
                         }
                    }
                }
             },
             "points": {
                "properties": {
                    "total_points":{
                        "type": "integer"
                    },
                    "available_points":{
                        "type": "integer"
                    },
                    "consum_points_cnt":{
                        "type": "integer"
                    },
                    "consum_points_max":{
                        "type": "integer"
                    },
                    "consum_points_min":{
                        "type": "integer"
                    },
                    "consum_points_sum":{
                        "type": "integer"
                    }
                }
             },
             "invest_repay_logger": {
                "properties": {
                    "currentperiod":{
                        "type": "long"
                    },
                    "repay_date":{
                        "format": "yyyy-MM-dd",
                        "type": "date"
                    },
                    "repay_amount":{
                        "type": "double"
                    }
                }
             },
             "enabled": {
                 "type": "integer"
             },
             "birth_date": {
                 "type": "integer"
             },
             "available_points": {
                 "type": "integer"
             },
             "enterprise": {
                 "type": "integer"
             },
             "source": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "email": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "login_name": {
                 "index": "not_analyzed",
                 "type": "string"
             },
             "mobile": {
                 "index": "not_analyzed",
                 "type": "string"
             }
         }
     }
 }'

