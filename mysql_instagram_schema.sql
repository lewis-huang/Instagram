create table Instagram_Pic_Url(
	ID int not null auto_increment,
    PicUrl VARCHAR(500),
    Downloaded VARCHAR(1),
	primary key(ID)
);

    

     drop procedure  Instagram_Pic_Url_Add ;
  DELIMITER //
  
  CREATE PROCEDURE Instagram_Pic_Url_Add (
	 PicUrl VARCHAR(500)
   
    )
  BEGIN 
	
    IF ( PicUrl IS NOT NULL) Then
		INSERT INTO Instagram_Pic_Url(PicUrl,Downloaded) VALUES(PicUrl,0) ;
    End IF ;
  
  END //
  DELIMITER ;
  
  
  set @PicUrl = 'www.baidu.com';
  Call Instagram_Pic_Url_Add(@PicUrl) ;
  
  
  select * from Instagram_Pic_Url
  truncate table Instagram_Pic_Url
  
  
  
     drop procedure  Instagram_Pic_Url_Getlist ;
  DELIMITER //
  
  CREATE PROCEDURE Instagram_Pic_Url_Getlist (
	    
    )
  BEGIN 
	
   SELECT * FROM Instagram_Pic_Url WHERE Downloaded = 0 ;
  
  END //
  DELIMITER ;
  
  Call Instagram_Pic_Url_Getlist() ;