-- CREATE DATABASE MacsDB;
-- USE MacsDB;
-- go;

-- CREATE SCHEMA VehicleLoad;
-- go;

DROP TABLE IF EXISTS MacsDB.VehicleLoad.tab_collection_data;
CREATE TABLE MacsDB.VehicleLoad.tab_collection_data (
    id BIGINT PRIMARY KEY IDENTITY(1,1),
    vin VARCHAR(20) NULL,
    clt_timestamp BIGINT NULL,
    longitude FLOAT NULL ,
    latitude FLOAT NULL ,
    status FLOAT NULL,
    altitude FLOAT NULL ,
    speed FLOAT NULL ,
    SOEO0001 FLOAT NULL ,
    SOEO0002 FLOAT NULL ,
    SOBS0003 FLOAT NULL ,
    SOBC0004 FLOAT NULL ,
    SOBC0005 FLOAT NULL ,
    SOBC0006 FLOAT NULL ,
    SOBC0007 FLOAT NULL ,
    SOBC0008 FLOAT NULL ,
    SOVR0009 FLOAT NULL ,
    SOVR0010 FLOAT NULL ,
    SOVR0011 FLOAT NULL ,
    SOBC0017 FLOAT NULL ,
    SOVR0019 FLOAT NULL ,
    SOBC0018 FLOAT NULL ,
    SOBP0021 FLOAT NULL ,
    SOBP0022 FLOAT NULL ,
    SOBP0023 FLOAT NULL ,
    SOBS0024 FLOAT NULL ,
    SOBR0025 FLOAT NULL ,
    SOBR0026 FLOAT NULL ,
    SOEI0027 FLOAT NULL ,
    SOEI0028 FLOAT NULL ,
    SOEI0029 FLOAT NULL ,
    SOEI0030 FLOAT NULL ,
    SOBR0032 FLOAT NULL ,
    SOBR0033 FLOAT NULL ,
    SOBR0035 FLOAT NULL ,
    SOBR0036 FLOAT NULL ,
    SOBR0037 FLOAT NULL ,
    SOBR0038 FLOAT NULL ,
    SOBR0039 FLOAT NULL ,
    SOBR0040 FLOAT NULL ,
    SOBR0041 FLOAT NULL ,
    SOBR0042 FLOAT NULL ,
    SOBR0043 FLOAT NULL ,
    SOBR0044 FLOAT NULL ,
    SOEI0046 FLOAT NULL ,
    SOBR0048 FLOAT NULL ,
    SOEI0047 FLOAT NULL ,
    SOBR0049 FLOAT NULL ,
    SOBR0050 FLOAT NULL ,
    SOBR0051 FLOAT NULL ,
    SOEI0052 FLOAT NULL ,
    SOBR0053 FLOAT NULL ,
    SOBR0054 FLOAT NULL ,
    SOEI0055 FLOAT NULL ,
    SOEI0056 FLOAT NULL ,
    SOEI0057 FLOAT NULL ,
    SOBR0058 FLOAT NULL ,
    SOBR0059 FLOAT NULL ,
    SOBR0060 FLOAT NULL ,
    SOBR0061 FLOAT NULL ,
    SOEI0062 FLOAT NULL ,
    SOBR0063 FLOAT NULL ,
    SOBR0064 FLOAT NULL ,
    SOBR0065 FLOAT NULL ,
    SOVR0066 FLOAT NULL ,
    SOEI0067 FLOAT NULL ,
    SOEI0068 FLOAT NULL ,
    SOBR0073 FLOAT NULL ,
    SOBR0071 FLOAT NULL ,
    SOBR0074 FLOAT NULL ,
    SOBR0075 FLOAT NULL ,
    SOBR0076 FLOAT NULL ,
    SOBR0087 FLOAT NULL ,
    SOBR0088 FLOAT NULL ,
    SOBR0089 FLOAT NULL ,
    SOBR0091 FLOAT NULL ,
    SOBR0092 FLOAT NULL ,
    SOEI0094 FLOAT NULL ,
    SOEI0095 FLOAT NULL ,
    SOBR0100 FLOAT NULL ,
    SOBR0104 FLOAT NULL ,
    SOBR0106 FLOAT NULL ,
    SOBR0107 FLOAT NULL ,
    SOBR0111 FLOAT NULL ,
    SOBR0116 FLOAT NULL ,
    SOBR0117 FLOAT NULL ,
    SOBR0118 FLOAT NULL ,
    SOBR0122 FLOAT NULL ,
    SOBC0125 FLOAT NULL ,
    SOBP0129 FLOAT NULL ,
    SOBP0130 FLOAT NULL ,
    SOBP0131 FLOAT NULL ,
    SOBP0132 FLOAT NULL ,
    SOBR0137 FLOAT NULL ,
    SOBR0142 FLOAT NULL ,
    SOFR1014 FLOAT NULL ,
    SOFR1015 FLOAT NULL ,
    SOBR0166 FLOAT NULL ,
    SOEI0176 FLOAT NULL ,
    SSBS3016 FLOAT NULL ,
    SSEI3017 FLOAT NULL ,
    SOBR0152 FLOAT NULL ,
    create_time DATETIME NOT NULL DEFAULT(GETDATE()),
    update_time DATETIME NOT NULL DEFAULT(GETDATE()),
    INDEX idx_vin_clt_timestamp (vin, clt_timestamp, speed)
);
