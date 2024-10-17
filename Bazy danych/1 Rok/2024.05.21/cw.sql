--zmiana typu bazy danych na 'Full'

use msdb;
GO

SELECT * FROM backupset


--Tasks -> Restore -> Options -> Close existing connections to destination database          (przed restore)


--------------------------------

-- Full Backup 
BACKUP DATABASE AdventureWorks2019
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backupDatabase.bak'
WITH FORMAT, MEDIANAME = 'SQLServerBackups',
NAME = 'Pełny Backup AdventureWorks2019';


-- Differential Backup 
BACKUP DATABASE AdventureWorks2019
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backupDatabase.bak'
WITH DIFFERENTIAL, 
MEDIANAME = 'SQLServerBackups',
NAME = 'Differential Backup AdventureWorks2019';


-- Log Backup 
BACKUP LOG AdventureWorks2019
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backupDatabase.bak' 
WITH FORMAT, MEDIANAME = 'SQLServerBackups',
NAME = 'Log Backup AdventureWorks2019';


--------------------------------

-- (nie działa)
-- Restore Bazy Danych
use master;
GO

ALTER DATABASE [AdventureWorks2019] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

RESTORE DATABASE AdventureWorks2019
FROM DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\backupDatabase.bak'
WITH NORECOVERY;

ALTER DATABASE [AdventureWorks2019] SET MULTI_USER;
