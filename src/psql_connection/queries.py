class Queries:
    cielo_transactions = """
        select
            t.transaction_id,
            t.create_by_user_id as user_id,
            t.status,
            cs.response::jsonb #>> '{{Payment,Installments}}' as installments,
            cast(cs.response::jsonb #>> '{{Payment,Amount}}' as float)/100 as amount,
            ma.score,
            count(t2.ticket_id) as count_tickets,
            ts.event_id,
            e.name,
            to_char(t.created_time at time zone 'UTC' at time zone 'US/Central', 'DD/MM/YYYY HH:MM') as captured_date
        from paguemob.cielo_statements cs
        inner join paguemob.transactions t on t.transaction_id = cs.reference_id
        inner join paguemob.maxmind_analysis ma on ma.transaction_group_id = t.group_id
        inner join events.tickets t2 on t2.transaction_group_id = t.group_id
        inner join events.ticket_specifications ts on ts.ticket_specification_id = t2.ticket_specification_id
        inner join events.events e on e.event_id = ts.event_id
        where cs.response::jsonb #>> '{{Payment,Tid}}' in {}
            and cs.event_type = 'authorization'
            and cs.status_code = 201
        group by 1,2,3,4,5,6,8,9,10
    """

    users = """
    select
        u.user_id,
        u.name,
        e.email,
        concat(ba.response::jsonb #>> '{{Result,0,BasicData,InputNameMatchPercentage}}', ' %') as cpf_match_percentage,
        count(a.account_id) as count_credit_card,
        to_char(u.created_time at time zone 'UTC' at time zone 'US/Central', 'DD/MM/YYYY') as created_at
    from paguemob.users u
    inner join paguemob.emails e on e.account_group_id = u.account_group_id
    inner join paguemob.accounts a on a.account_group_id  = u.account_group_id
    inner join paguemob.bigdatacorp_analysis ba on ba.user_id = u.user_id
    where u.user_id in {}
        and a.account_type <> 1
    group by 1,2,3,4,6
    order by u.created_time desc
    limit 10
    """
