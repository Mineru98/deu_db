CREATE TABLE "Artist" (
	"artist_id" NUMBER (20) NOT NULL,
	"company_id" NUMBER (20) NOT NULL,
	"artist_name" VARCHAR2 (128) NULL,
	"solo_act_status" NUMBER (1) DEFAULT 0 NULL
);

COMMENT ON COLUMN "Artist"."artist_id" IS '가수 ID';

COMMENT ON COLUMN "Artist"."company_id" IS '소속사 ID';

COMMENT ON COLUMN "Artist"."artist_name" IS '활동명';

COMMENT ON COLUMN "Artist"."solo_act_status" IS '솔로활동여부';

CREATE TABLE "Company" (
	"company_id" NUMBER (20) NOT NULL,
	"company_name" VARCHAR2 (128) NULL,
	"year_estbl" DATE DEFAULT SYSDATE NULL
);

COMMENT ON COLUMN "Company"."company_id" IS '소속사 ID';

COMMENT ON COLUMN "Company"."company_name" IS '회사명';

COMMENT ON COLUMN "Company"."year_estbl" IS '설립연도';

CREATE TABLE "Fan" (
	"fan_id" NUMBER (20) NOT NULL,
	"fan_name" VARCHAR2 (28) NOT NULL,
	"gender" CHAR(12) NOT NULL,
	"birthday" DATE DEFAULT SYSDATE NULL,
	"location" VARCHAR2 (28) NOT NULL
);

COMMENT ON COLUMN "Fan"."fan_id" IS '팬 ID';

COMMENT ON COLUMN "Fan"."fan_name" IS '이름';

COMMENT ON COLUMN "Fan"."gender" IS '성별';

COMMENT ON COLUMN "Fan"."birthday" IS '생년월일';

COMMENT ON COLUMN "Fan"."location" IS '거주지';

CREATE TABLE "Concert" (
	"concert_id" NUMBER (20) NOT NULL,
	"concert_title" VARCHAR2 (128) NOT NULL,
	"concert_date" DATE DEFAULT SYSDATE NULL,
	"capacity" NUMBER DEFAULT 0 NULL,
	"artist_id" NUMBER (20) NOT NULL,
	"company_id" NUMBER (20) NOT NULL
);

COMMENT ON COLUMN "Concert"."concert_id" IS '콘서트 ID';

COMMENT ON COLUMN "Concert"."concert_title" IS '콘서트 제목';

COMMENT ON COLUMN "Concert"."concert_date" IS '콘서트 날짜';

COMMENT ON COLUMN "Concert"."capacity" IS '콘서트 최대 인원';

COMMENT ON COLUMN "Concert"."artist_id" IS '가수 ID';

COMMENT ON COLUMN "Concert"."company_id" IS '소속사 ID';

CREATE TABLE "Album" (
	"album_id" NUMBER (20) NOT NULL,
	"album_title" VARCHAR2 (128) NULL,
	"album_pbl_date" DATE DEFAULT SYSDATE NULL,
	"artist_id" NUMBER (20) NOT NULL,
	"company_id" NUMBER (20) NOT NULL
);

COMMENT ON COLUMN "Album"."album_id" IS '앨범 ID';

COMMENT ON COLUMN "Album"."album_title" IS '앨범제목';

COMMENT ON COLUMN "Album"."album_pbl_date" IS '앨범 공개 일시';

COMMENT ON COLUMN "Album"."artist_id" IS '가수 ID';

COMMENT ON COLUMN "Album"."company_id" IS '소속사 ID';

CREATE TABLE "AlbumSales" (
	"album_id" NUMBER (20) NOT NULL,
	"fan_id" NUMBER (20) NOT NULL,
	"price" NUMBER DEFAULT 0 NULL,
	"payment_date" DATE DEFAULT SYSDATE NULL,
	"is_canceled" NUMBER (1) DEFAULT 0 NULL
);

COMMENT ON COLUMN "AlbumSales"."album_id" IS '앨범 ID';

COMMENT ON COLUMN "AlbumSales"."fan_id" IS '팬 ID';

COMMENT ON COLUMN "AlbumSales"."price" IS '가격';

COMMENT ON COLUMN "AlbumSales"."payment_date" IS '구매날짜';

COMMENT ON COLUMN "AlbumSales"."is_canceled" IS '취소여부';

CREATE TABLE "ConcertTicket" (
	"fan_id" NUMBER (20) NOT NULL,
	"concert_id" NUMBER (20) NOT NULL,
	"ticket_price" NUMBER DEFAULT 0 NULL,
	"sheet_level" VARCHAR(255) NULL,
	"sheet_num" CHAR(5) NOT NULL,
	"payment_date" DATE DEFAULT SYSDATE NULL,
	"is_canceled" NUMBER (1) DEFAULT 0 NULL
);

COMMENT ON COLUMN "ConcertTicket"."fan_id" IS '팬 ID';

COMMENT ON COLUMN "ConcertTicket"."concert_id" IS '콘서트 ID';

COMMENT ON COLUMN "ConcertTicket"."ticket_price" IS '가격';

COMMENT ON COLUMN "ConcertTicket"."sheet_level" IS '좌석등급';

COMMENT ON COLUMN "ConcertTicket"."sheet_num" IS '좌석번호';

COMMENT ON COLUMN "ConcertTicket"."payment_date" IS '구매날짜';

COMMENT ON COLUMN "ConcertTicket"."is_canceled" IS '취소여부';

CREATE TABLE "Song" (
	"song_id" NUMBER (20) NOT NULL,
	"song_name" VARCHAR2 (256) NOT NULL,
	"play_time" NUMBER DEFAULT 0 NULL
);

COMMENT ON COLUMN "Song"."song_id" IS '노래 ID';

COMMENT ON COLUMN "Song"."song_name" IS '노래제목';

COMMENT ON COLUMN "Song"."play_time" IS '재생시간';

CREATE TABLE "AlbumTract" (
	"album_id" NUMBER (20) NOT NULL,
	"song_id" NUMBER (20) NOT NULL,
	"order_num" NUMBER NOT NULL
);

COMMENT ON COLUMN "AlbumTract"."album_id" IS '앨범 ID';

COMMENT ON COLUMN "AlbumTract"."song_id" IS '노래 ID';

COMMENT ON COLUMN "AlbumTract"."order_num" IS '수록순서';

CREATE TABLE "ConcertTract" (
	"song_id" NUMBER (20) NOT NULL,
	"concert_id" NUMBER (20) NOT NULL,
	"order_num" NUMBER NOT NULL
);

COMMENT ON COLUMN "ConcertTract"."song_id" IS '노래 ID';

COMMENT ON COLUMN "ConcertTract"."concert_id" IS '콘서트 ID';

COMMENT ON COLUMN "ConcertTract"."order_num" IS '진행 순서';

ALTER TABLE "Artist"
	ADD CONSTRAINT "PK_ARTIST" PRIMARY KEY ("artist_id");

ALTER TABLE "Company"
	ADD CONSTRAINT "PK_COMPANY" PRIMARY KEY ("company_id");

ALTER TABLE "Fan"
	ADD CONSTRAINT "PK_FAN" PRIMARY KEY ("fan_id");

ALTER TABLE "Concert"
	ADD CONSTRAINT "PK_CONCERT" PRIMARY KEY ("concert_id");

ALTER TABLE "Album"
	ADD CONSTRAINT "PK_ALBUM" PRIMARY KEY ("album_id");

ALTER TABLE "AlbumSales"
	ADD CONSTRAINT "PK_ALBUMSALES" PRIMARY KEY ("album_id", "fan_id");

ALTER TABLE "ConcertTicket"
	ADD CONSTRAINT "PK_CONCERTTICKET" PRIMARY KEY ("fan_id", "concert_id");

ALTER TABLE "Song"
	ADD CONSTRAINT "PK_SONG" PRIMARY KEY ("song_id");

ALTER TABLE "Artist"
	ADD CONSTRAINT "FK_Artist_TO_Company_1" FOREIGN KEY ("company_id") REFERENCES "Company" ("company_id");

ALTER TABLE "Concert"
	ADD CONSTRAINT "FK_Artist_TO_Concert_1" FOREIGN KEY ("artist_id") REFERENCES "Artist" ("artist_id");

ALTER TABLE "Concert"
	ADD CONSTRAINT "FK_Concert_TO_Company_1" FOREIGN KEY ("company_id") REFERENCES "Company" ("company_id");

ALTER TABLE "Album"
	ADD CONSTRAINT "FK_Artist_TO_Album_1" FOREIGN KEY ("artist_id") REFERENCES "Artist" ("artist_id");

ALTER TABLE "Album"
	ADD CONSTRAINT "FK_Company_TO_Album_1" FOREIGN KEY ("company_id") REFERENCES "Company" ("company_id");

ALTER TABLE "AlbumSales"
	ADD CONSTRAINT "FK_Album_TO_AlbumSales_1" FOREIGN KEY ("album_id") REFERENCES "Album" ("album_id");

ALTER TABLE "AlbumSales"
	ADD CONSTRAINT "FK_Fan_TO_AlbumSales_1" FOREIGN KEY ("fan_id") REFERENCES "Fan" ("fan_id");

ALTER TABLE "ConcertTicket"
	ADD CONSTRAINT "FK_Fan_TO_ConcertTicket_1" FOREIGN KEY ("fan_id") REFERENCES "Fan" ("fan_id");

ALTER TABLE "ConcertTicket"
	ADD CONSTRAINT "FK_Concert_TO_ConcertTicket_1" FOREIGN KEY ("concert_id") REFERENCES "Concert" ("concert_id");

ALTER TABLE "AlbumTract"
	ADD CONSTRAINT "FK_Album_TO_AlbumTract_1" FOREIGN KEY ("album_id") REFERENCES "Album" ("album_id");

ALTER TABLE "AlbumTract"
	ADD CONSTRAINT "FK_Song_TO_AlbumTract_1" FOREIGN KEY ("song_id") REFERENCES "Song" ("song_id");

ALTER TABLE "AlbumTract"
	ADD CONSTRAINT "PK_ALBUMTRACT" PRIMARY KEY ("album_id", "song_id");

ALTER TABLE "ConcertTract"
	ADD CONSTRAINT "FK_Song_TO_ConcertTract_1" FOREIGN KEY ("song_id") REFERENCES "Song" ("song_id");

ALTER TABLE "ConcertTract"
	ADD CONSTRAINT "FK_Concert_TO_ConcertTract_1" FOREIGN KEY ("concert_id") REFERENCES "Concert" ("concert_id");
	
ALTER TABLE "ConcertTract"
	ADD CONSTRAINT "PK_CONCERTTRACT" PRIMARY KEY ("song_id", "concert_id");