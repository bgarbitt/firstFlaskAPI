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

API methods
==========
questions
---------
* create a question (a POST method)\
    *url*/createQuestion/prompt/choices/solution/zone/branch/qtype/ilink/slink/blanks
    - prompt = question/task for user
    - choices = choices a user gets if type is multChoice
    - solution = solution to question/task
    - zone = zone of library (Nonfiction, fiction, etc). A foreign key to zones in the zone table.
    - branch = library branch (Clareview, Highlands, etc.). A foreign key to branches in the zone table.
    - qtype = question type (multChoice, writInput, picInput)
    - ilink = image internet url
    - slink = sound internet url
    - blanks = similar to solution with targeted underscores (_ru_pet Chanete_elle)

* delete a question (a DELETE method)\
    *url*/deleteQuestion/id
    - id = a unique id for an individual question. id is a primary key for questions.

* get question (a GET method)\
    *url*/getQuestion/zone/branch
    - zone = zone of library. A foreign key to zones in the zone table.
    branch = branch of library. A foreign key to branches in the zone table.

* get all questions (a GET method)\
    *url*/getAllQuestions/
    - **NOT** Currently utilized in web app or android app (Nov 30, 2017)

* update a question (a POST method)\
    *url*/updateQuestion/id/prompt/choices/solution/zone/branch/qtype/ilink/slink/blanks
    - id = a unique id for an individual question. id is a primary key for questions.
    - prompt = question/task for user
    - choices = choices a user gets if type is multChoice
    - solution = solution to question/task
    - zone = zone of library (Nonfiction, fiction, etc). A foreign key to zones in the zone table.
    - branch = library branch (Clareview, Highlands, etc.). A foreign key to branches in the zone table.
    - qtype = question type (multChoice, writInput, picInput)
    - ilink = image internet url
    - slink = sound internet url
    - blanks = similar to solution with targeted underscores (_ru_pet Chanete_elle)

zones
-----
* create a zone (a POST method)\
    *url*/createZone/new_beaconID/new_zone/new_branch/new_category/new_color
    - new_beaconID = id of the beacon devices supplied by EPL.
    - new_zone = zone being added to library.
    - new_branch = branch of library. A foreign key to branches in the branch table.
    - new_category = category of the questions in zone (cats, wildlife, etc.)
    - new_color = a hex value of a color.

* get a zone (a GET method)\
    *url*/getZone/branch
    - branch = branch of library. A foreign key to branches in the branch table.

* delete a zone (a DELETE method)\
    *url*/zone/branch
    - zone = zone of library.
    - branch = branch of library.

* update a zone (a POST method)\
    *url*/updateZone/new_beaconID/old_zone/new_zone/old_branch/new_branch/new_category/new_color
    - new_beaconID = id of the beacon devices supplied by EPL.
    - old_zone = zone name before update
    - new_zone = zone name after update
    - old_branch = branch name before update. A foreign key to branches in the branch table.
    - new_branch = branch name after update. A foreign key to branches in the branch table.
    - new_category = category of the questions in zone (cats, wildlife, etc.)
    - new_color = a hex value of a color.

branches
--------
* create a library branch (a POST method)\
    *url*/createBranch/new_branch/new_iLink
    - new_branch = new library branch to be added. A primary key.
    - new_iLink = image internet url of library branch.

* delete a branch (a DELETE method)\
    *url*/deleteBranch/branch
    - branch = branch to be deleted. A primary key.\
    ***WARNING:*** deleting a branch deletes all the zones and questions associated with it.

* get all branches in the database (a GET method)\
    *url*/getBranch/
    - utilized by web app for dashboard/home page.

* update a branch (a POST method)\
    *url*/updateBranch/oldBranch/newBranch/iLink
    - oldBranch = branch that is currently in database.
    - newBranch = new branch name
    - iLink = new image internet url
