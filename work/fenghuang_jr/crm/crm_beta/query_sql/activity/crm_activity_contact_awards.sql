use crm_v2
insert overwrite table activity_contact_awards
SELECT
    activity_contact_awards.*
FROM
(
    SELECT * FROM activity_contact_awards_0

    UNION ALL

    SELECT * FROM activity_contact_awards_1

    UNION ALL

    SELECT * FROM activity_contact_awards_2

    UNION ALL

    SELECT * FROM activity_contact_awards_3

    UNION ALL

    SELECT * FROM activity_contact_awards_4

    UNION ALL

    SELECT * FROM activity_contact_awards_5

    UNION ALL

    SELECT * FROM activity_contact_awards_6

    UNION ALL

    SELECT * FROM activity_contact_awards_7

    UNION ALL

    SELECT * FROM activity_contact_awards_8

    UNION ALL

    SELECT * FROM activity_contact_awards_9

    UNION ALL

    SELECT * FROM activity_contact_awards_10

    UNION ALL

    SELECT * FROM activity_contact_awards_11

    UNION ALL

    SELECT * FROM activity_contact_awards_12

    UNION ALL

    SELECT * FROM activity_contact_awards_13

    UNION ALL

    SELECT * FROM activity_contact_awards_14

    UNION ALL

    SELECT * FROM activity_contact_awards_15
 ) AS activity_contact_awards
 WHERE activity_contact_awards.deleted = 0 and \$CONDITIONS
