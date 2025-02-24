# -- 查找用户id以及相对应的名称
# select user_id, user_name 
# from events
# group by user_id,user_name
# order by user_id

# -- 查找对应user_id 用户
# SELECT user_id, task_id, job_id, any_value(user_name), sum(count)
# FROM cvat.events
# WHERE scope = 'create:shapes'
#   AND timestamp > '2024-12-17'
#   AND timestamp < '2024-12-18'
#   AND user_id = 1
# GROUP BY user_id, task_id, job_id
# # ORDER BY user_id;