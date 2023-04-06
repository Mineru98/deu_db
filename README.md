# deu_db

## 이미지 설치 및 실행

```bash
docker-compose up -d

docker exec -it oracle sqlplus
```

user-name 부분에 `sys as sysdba`라고 입력한다. 이것의 의미는 관리자로 접근하겠다는 의미.
Enter password 부분에는 `oracle`이라고 입력한다.

```txt
$ docker exec -it oracle sqlplus

$ SQL*Plus: Release 12.1.0.2.0 Production on Thu Apr 6 14:07:18 2023

$ Copyright (c) 1982, 2014, Oracle.  All rights reserved.

$ Enter user-name: sys as sysdba
$ Enter password: 

$ Connected to:
$ Oracle Database 12c Standard Edition Release 12.1.0.2.0 - 64bit Production

$ SQL>
```

다음으로 아래와 같이 입력한다. 그러면 `user1` 이라는 계정의 비밀번호는 `userpwd`가 된다.

```sql
CREATE USER user1 identified BY userpwd;

GRANT connect, resource, dba TO user1;

COMMIT;

SELECT
	*
FROM
	all_users;
```
