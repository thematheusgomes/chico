class Queries:
    select = """
        SELECT *
        FROM paguemob.users
        LIMIT 10;
    """
    cielo = """
        SELECT cs.response::jsonb #>> '{Payment,Tid}' AS "tid",'https://vamoapp.com/admin/users/' || u.user_id AS "user",
        'https://vamoapp.com/admin/transactions/' || t2.transaction_id AS "transaction", 
        CASE t2.status
            WHEN 6 THEN 'Captured'
            WHEN 9 THEN 'Refunded'
            WHEN 26 THEN 'PartialRefund'
            WHEN 28 THEN 'Refunded-Fraud'
            ELSE '' || t2.status
        END AS status,
        ev.name AS "event"
        FROM paguemob.cielo_statements AS cs
        INNER JOIN paguemob.transactions AS t 
        ON t.transaction_id = cs.reference_id
        INNER JOIN paguemob.users AS u 
        ON t.create_by_user_id = u.user_id
        INNER JOIN events.tickets AS tk
            ON t.group_id = tk.transaction_group_id
        INNER JOIN events.ticket_specifications AS ts 
        ON ts.ticket_specification_id = tk.ticket_specification_id
        INNER JOIN events.events AS ev 
        ON ev.event_id = ts.event_id
        INNER JOIN paguemob.maxmind_analysis as ma
                ON ma.user_id = u.user_id
        INNER JOIN paguemob.transactions AS t2
            ON t2.group_id = t.group_id AND t2.type = 3         
        WHERE cs.response::jsonb #>> '{Payment,Tid}' IN (%s)
            AND cs.response <> ''
            AND cs.event_type = 'authorization'
            AND status_code = 201
        GROUP BY u.user_id, t2.transaction_id,t.amount, ts.type, tk.status, tk.ticket_specification_id, ev.name, ev.start_time, cs.response
    """
