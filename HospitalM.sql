create database aidata;
use aidata;
CREATE TABLE hospitalm (
    nameoftablets VARCHAR(255) not null,
    ref VARCHAR(255) PRIMARY KEY not null,
    dose VARCHAR(255),
    nooftablets VARCHAR(255),
    lot VARCHAR(255),
    issuedate VARCHAR(255),
    expdate VARCHAR(255),
    dailydose VARCHAR(255),
    storage VARCHAR(255),
    nhsnumber VARCHAR(255),
    pname VARCHAR(255),
    dob VARCHAR(255),
    address VARCHAR(255)
);