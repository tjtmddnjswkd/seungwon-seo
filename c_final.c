#include <stdio.h>

int main(void) {

	char zero[7] = "ABCDEFG";
	char one[7] = "HIJKLMN";
	char two[7] = "OPQRSTU";
	char three[5] = "VWXYZ";
	char four[7] = "abcdefg";
	char five[7] = "hijklmn";
	char six[7] = "opqrstu";
	char seven[5] = "vwxyz";
	char ch;
	int i = 0;
	int len = 0; /*문자를 받을때 맨처음과 그이후를 구별하기위한 변수*/
	int be_g,re_g; /*이전 문자의 그룹과 현재 입력받은 문자의 그룹*/

	char re; /* 현재 입력받은 문자.*/
	printf("변환시킬 문자열을 입력하세요.\n");
	while ((ch = getchar()) != EOF) {
		if (len == 0) {
			re = ch;
			len++;
			if (re == ' ') {
				printf("8");
				continue;
			}
			for (int ind = 0; ind < 7; ind++) {			/* 그룹을 정해주는 코드.*/
				if (zero[ind] == re) {
					re_g = 0;
					be_g = 0;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (one[ind] == re) {
					re_g = 1;
					be_g = 1;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (two[ind] == re) {
					re_g = 2;
					be_g = 2;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (three[ind] == re) {
					re_g = 3;
					be_g = 3;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (four[ind] == re) {
					re_g = 4;
					be_g = 4;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (five[ind] == re) {
					re_g = 5;
					be_g = 5;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (six[ind] == re) {
					re_g = 6;
					be_g = 6;
					i = ind;
				}
			}
			for (int ind = 0; ind < 5; ind++) {
				if (seven[ind] == re) {
					re_g = 7;
					be_g = 7;
					i = ind;
				}
			}
			printf("변환된 숫자코드\n");
			if (re_g == 0) {			/*문자의 그룹과 반복수를 이용해 해당 알파벳에 대한 숫자코드 출력*/
				for (int ind = 0; ind <= i; ind++)
					printf("0");
			}
			if (re_g == 1) {
				for (int ind = 0; ind <=i; ind++)
					printf("1");
			}
			if (re_g == 2) {
				for (int ind = 0; ind <=i; ind++)
					printf("2");
			}
			if (re_g == 3) {
				for (int ind = 0; ind <=i; ind++)
					printf("3");
			}
			if (re_g == 4) {
				for (int ind = 0; ind <=i; ind++)
					printf("4");
			}
			if (re_g == 5) {
				for (int ind = 0; ind <=i; ind++)
					printf("5");
			}
			if (re_g == 6) {
				for (int ind = 0; ind <=i; ind++)
					printf("6");
			}
			if (re_g == 7) {
				for (int ind = 0; ind <=i; ind++)
					printf("7");
			}
		}
		else { /*len이 0이 아닐때(맨처음에는 be_g 때문에 조금 다름)*/
			i = 0;
			re = ch;

			if (re == '\n') /*엔터누르면 종료*/
				break;
			if (re == ' ') { /*스페이스는 8출력*/
				printf("8");
				continue;
			}
				
			for (int ind = 0; ind < 7; ind++) { /*위와 비슷 해당 문자에 그룹과 반복수 할당.*/
				if (zero[ind] == re) {
					re_g = 0;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (one[ind] == re) {
					re_g = 1;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (two[ind] == re) {
					re_g = 2;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (three[ind] == re) {
					re_g = 3;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (four[ind] == re) {
					re_g = 4;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (five[ind] == re) {
					re_g = 5;
					i = ind;
				}
			}
			for (int ind = 0; ind < 7; ind++) {
				if (six[ind] == re) {
					re_g = 6;
					i = ind;
				}
			}
			for (int ind = 0; ind < 5; ind++) {
				if (seven[ind] == re) {
					re_g = 7;
					i = ind;
				}
			}
			if (re_g == be_g) { /*정해진 현재그룹 re_g 와 이전 문자의 그룹 be_g가 같으면 9출력*/
				printf("9");
				be_g = re_g;
			}
			be_g = re_g;
			if (re_g == 0) { /*현재 입력된 문자에 대한 숫자코드 출력*/
				for (int ind = 0; ind <= i; ind++)
					printf("0");
			}
			if (re_g == 1) {
				for (int ind = 0; ind <= i; ind++)
					printf("1");
			}
			if (re_g == 2) {
				for (int ind = 0; ind <= i; ind++)
					printf("2");
			}
			if (re_g == 3) {
				for (int ind = 0; ind <= i; ind++)
					printf("3");
			}
			if (re_g == 4) {
				for (int ind = 0; ind <= i; ind++)
					printf("4");
			}
			if (re_g == 5) {
				for (int ind = 0; ind <= i; ind++)
					printf("5");
			}
			if (re_g == 6) {
				for (int ind = 0; ind <= i; ind++)
					printf("6");
			}
			if (re_g == 7) {
				for (int ind = 0; ind <= i; ind++)
					printf("7");
			}
		}
	}

	return 0;
}