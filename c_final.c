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
	int len = 0; /*���ڸ� ������ ��ó���� �����ĸ� �����ϱ����� ����*/
	int be_g,re_g; /*���� ������ �׷�� ���� �Է¹��� ������ �׷�*/

	char re; /* ���� �Է¹��� ����.*/
	printf("��ȯ��ų ���ڿ��� �Է��ϼ���.\n");
	while ((ch = getchar()) != EOF) {
		if (len == 0) {
			re = ch;
			len++;
			if (re == ' ') {
				printf("8");
				continue;
			}
			for (int ind = 0; ind < 7; ind++) {			/* �׷��� �����ִ� �ڵ�.*/
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
			printf("��ȯ�� �����ڵ�\n");
			if (re_g == 0) {			/*������ �׷�� �ݺ����� �̿��� �ش� ���ĺ��� ���� �����ڵ� ���*/
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
		else { /*len�� 0�� �ƴҶ�(��ó������ be_g ������ ���� �ٸ�)*/
			i = 0;
			re = ch;

			if (re == '\n') /*���ʹ����� ����*/
				break;
			if (re == ' ') { /*�����̽��� 8���*/
				printf("8");
				continue;
			}
				
			for (int ind = 0; ind < 7; ind++) { /*���� ��� �ش� ���ڿ� �׷�� �ݺ��� �Ҵ�.*/
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
			if (re_g == be_g) { /*������ ����׷� re_g �� ���� ������ �׷� be_g�� ������ 9���*/
				printf("9");
				be_g = re_g;
			}
			be_g = re_g;
			if (re_g == 0) { /*���� �Էµ� ���ڿ� ���� �����ڵ� ���*/
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