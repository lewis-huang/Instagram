1. 一张主表，用来记录需要爬取的专栏名称，专栏URL地址。
专栏名称将作为文件夹，保存在g:\cartoon\desktop 总目录下。
专栏URL，就会被爬虫爬取每一张图片的URL, 经由爬虫的多线程下载器，下载到本地的专栏名称文件夹下

2. 多张子表：
2.1 爬取历史记录：专栏爬取的时间，用时，爬取数目
2.2 爬取的异常：专栏爬取的每一张图片的url, 是否正常下载，异常原因
2.3 是否考虑将评论也爬取下来，调用翻译软件的api, 将评论翻译成中文

create table instagramColumnList(
	ID int not null auto_increment primary key,
    ColumnName nvarchar(200) ,
    ColumnUrl varchar(2000) ,
	Crawled int  
    ) ;
    
delimiter //    
create procedure insertNewColumn (
	pColumnName NVARCHAR(200),
    pColumnUrl varchar(2000)
)
begin
	if (not exists(select 1 from instagramColumnList where ColumnName=pColumnName Limit 1 ) ) then
		insert into instagramColumnList(ColumnName,ColumnUrl,Crawled) Values(pColumnName,pColumnUrl,0) ;
	end if ;
end // 
delimiter ;

	
drop procedure 		insertNewColumn ;
delimiter //    
create procedure insertNewColumn (
	pColumnName NVARCHAR(200),
    pColumnUrl varchar(2000)
)
begin
	if (not exists(select 1 from instagramColumnList where ColumnName=pColumnName Limit 1 ) ) then
		insert into instagramColumnList(ColumnName,ColumnUrl,Crawled) Values(pColumnName,pColumnUrl,0) ;
	end if ;
end 
// delimiter ;


call insertNewColumn('Baidu','www.baidu.com') ;
select * from instagramColumnList ;

delimiter  //

create procedure getNewColumnList (
	LimitNumber int 
)
begin 
	select ColumnName,ColumnUrl 
    from instagramColumnList 
    where Crawled = 0 
    Limit LimitNumber ;
end 

//delimiter 

call getNewColumnList (20) ;



