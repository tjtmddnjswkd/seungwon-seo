#include <stdio.h>
#include <stdlib.h>


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
	int len = 0; /*��ó�� ���ڿ� �����ĸ� �����ϱ� ���� ����� ����*/

	printf("��ȯ�� ���ڸ� �Է��ϼ���.\n");
	char be, re; /*���� ���ڿ� �����Էµ� ���ڸ� �����ϱ� ���� be,re����*/
	be = 'x'; /*�ǹ̾��� �׳� �ƹ��ų� �Ҵ�*/
	while ((ch = getchar()) != EOF) {
		if (len == 0) {
			be = re = ch; /*��ó���� be�� re�� ���� �Ҵ�*/
			len++;
			printf("��ȯ�� �ؽ�Ʈ��\n");
			continue;
		}
		re = ch;
		if (re != be) { /*�����Էµ� ���ڿ� ���� �Էµ� ���ڰ� �ٸ��� �������� �Էµ� ���ڵ鿡 �����ϴ� ���ĺ� ���*/
			if (be == '1')
				printf("%c", one[i]);
			if (be == '2')
				printf("%c", two[i]);
			if (be == '3')
				printf("%c", three[i]);
			if (be == '4')
				printf("%c", four[i]);
			if (be == '5')
				printf("%c", five[i]);
			if (be == '6')
				printf("%c", six[i]);
			if (be == '7')
				printf("%c", seven[i]);
			if (be == '0')
				printf("%c", zero[i]);
			if (be == '9')
				printf("");
			if (be == '8')
				printf("%c", ' ');
			i = 0;
			be = re; /*����� be ������Ʈ*/
			continue;
		}
		if (re == '\n') {
			printf("\n");
			break;
		}
		i++;
		
			
	}
	

	
	return 0;
}

