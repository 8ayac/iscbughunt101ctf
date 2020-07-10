USE bughunt101;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    `id`        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username`  VARCHAR(32) NOT NULL,
    `password`  VARCHAR(128) NOT NULL
);

INSERT INTO users
    (username, password)
VALUES
    ('admin', '0eVMRxjRmCTVTbCFmZfVL0YUzOH02udzoc8VwcDCXVr9hqqdZjT2OVGfHxrrzMFvPrC2qrrEOmyGhZf329fBnGGMReFSCIngprmAgM74c46MISAuv2Lyebw1d0LUaZzn');
