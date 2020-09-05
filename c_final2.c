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
	int len = 0; /*맨처음 숫자와 그이후를 구별하기 위해 사용한 변수*/

	printf("변환할 숫자를 입력하세요.\n");
	char be, re; /*이전 숫자와 현재입력된 숫자를 구별하기 위해 be,re생성*/
	be = 'x'; /*의미없이 그냥 아무거나 할당*/
	while ((ch = getchar()) != EOF) {
		if (len == 0) {
			be = re = ch; /*맨처음에 be랑 re가 같게 할당*/
			len++;
			printf("변환된 텍스트는\n");
			continue;
		}
		re = ch;
		if (re != be) { /*이전입력된 숫자와 현재 입력된 숫자가 다를때 이전까지 입력된 숫자들에 대응하는 알파벳 출력*/
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
			be = re; /*출력후 be 업데이트*/
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

