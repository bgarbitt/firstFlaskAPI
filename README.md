# firstFlaskAPI

Cloned from https://realpython.com/blog/python/token-based-authentication-with-flask/ for authentication and setup. 
This API's methods are meant for the following schema:
==========================

    CREATE TABLE `questions` (
      `Prompt` text,
      `Choices` text,
      `Solution` text,
      `zone` varchar(30) DEFAULT NULL,
      `branch` varchar(30) DEFAULT NULL,
      `qType` text,
      `iLink` text,
      `sLink` text,
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `blanks` text,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`zone`) REFERENCES zone(`zone`) ON UPDATE CASCADE ON DELETE CASCADE,
      FOREIGN KEY (`branch`) REFERENCES zone(`branch`) ON UPDATE CASCADE ON DELETE CASCADE
    ) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

    CREATE TABLE `zone` (
      `beaconID` varchar(50) DEFAULT NULL,
      `zone` varchar(30) NOT NULL DEFAULT '',
      `branch` varchar(30) NOT NULL DEFAULT '',
      `category` text,
      `color` text,
      PRIMARY KEY (`zone`,`branch`),
      FOREIGN KEY (`branch`) REFERENCES `branch` (`branch`) ON UPDATE CASCADE ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

    CREATE TABLE `branch` (
      `branch` varchar(30) NOT NULL DEFAULT '',
      `prizeLocation` text,
      `iLink` text,
      PRIMARY KEY (`branch`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
