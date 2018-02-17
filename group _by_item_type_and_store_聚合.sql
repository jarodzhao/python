select store,item_type,count(*) count from faxian
group by store,item_type
order by store


