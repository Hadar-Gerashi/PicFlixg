CREATE DATABASE social_network
GO
USE social_network
GO
CREATE TABLE users
(
	users_id INT PRIMARY KEY IDENTITY(1,1),
	users_name VARCHAR(25) NOT NULL,
	email VARCHAR(50) UNIQUE CHECK(email like '%@%.%')NOT NULL,
	password_user VARCHAR(9) NOT NULL,
	created_at DATETIME  DEFAULT GETDATE() ,
	status_user INT DEFAULT 1,
	profile_image VARCHAR(255) NULL,
	profile_text VARCHAR(50) NULL
);

CREATE TABLE categories
(
    category_id INT PRIMARY KEY IDENTITY(1,1),
    category_name VARCHAR(25) UNIQUE  NOT NULL
);

CREATE TABLE videos
(
    video_id INT PRIMARY KEY IDENTITY(1,1) ,
    users_id INT FOREIGN KEY REFERENCES users(users_id) NOT NULL,
    video_url VARCHAR(255) NOT NULL,
    created_at DATETIME  DEFAULT GETDATE()
);

CREATE TABLE likes (
    like_id INT PRIMARY KEY IDENTITY(1,1),
    users_id INT NOT NULL,
    video_id INT NOT NULL,
    date_update DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (users_id) REFERENCES users(users_id),
    FOREIGN KEY (video_id) REFERENCES videos(video_id) ON DELETE CASCADE
);

CREATE TABLE category_video (
   video_id INT NOT NULL,
   category_id INT NOT NULL,
   PRIMARY KEY (video_id, category_id),
   FOREIGN KEY (video_id) REFERENCES videos(video_id),
   FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE user_categories (
   users_id INT NOT NULL,
   category_id INT NOT NULL,
   PRIMARY KEY (users_id, category_id),
   FOREIGN KEY (users_id) REFERENCES users(users_id),
   FOREIGN KEY (category_id) REFERENCES categories(category_id)
);




