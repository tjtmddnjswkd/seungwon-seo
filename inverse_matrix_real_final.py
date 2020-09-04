from fractions import Fraction #분수를 나타내기 위한 모듈

def get_and_show_matrix(n): #행렬을 입력하고 출력하는 함수
    for i in range(0,n):
        globals()['a{}'.format(i)]=[] #각 행에 대한 리스트를 생성.
        j=0
        while j<n:
            try:
                print('%d행의 성분을 한개씩 입력하세요'%(i+1))
                element=float(input()) #입력한 것이 숫자가 아니면 except문으로 간다.
                if int(element)==float(element): #입력한 숫자가 정수일 때는 정수로 저장.
                    globals()['a{}'.format(i)].append(int(element))
                    j+=1
                else:
                    globals()['a{}'.format(i)].append(Fraction(element)) #입력한 수가 실수일 때는 분수로 저장.
                    j+=1
            except:
                print('다시 입력하세요. 숫자만 가능합니다.')
                continue
    print('matrix is')
    for i in range(0,n): #입력받은 리스트들 쫙 출력. (= 행렬 출력)
        print(globals()['a{}'.format(i)])
    while 1:
        answer=input('Is matrix alright?(Y/N)') # 입력한게 맞는지 확인. 만약 아니면 다시 처음부터 입력.
        if answer.upper()=='N':
            print('행렬을 다시 생성합니다.')
            get_and_show_matrix(n)
        elif answer.upper()=='Y':
            break
        else:
            print('y 또는 n만 입력가능합니다.')
            continue

def define_n(): # nXn 의 n을 결정하는 함수.
    while 1:
        print('역행렬 찾는 프로그램입니다')
        try: # 정수만 입력가능. 정수 이외에는 불가능. 0도 안됌.
            n=float(input('n x n의 n을 입력하세요.'))
            if n==0:
                print('불가능합니다. 양의 정수를 다시 입력해주세요')
            elif int(n)!=n:
                print('양의 정수만 입력하세요.')
            elif n>0:
                n=int(n)
                print('%d x %d 행렬을 만듭니다.'%(n,n))
                return n
                break
        except:
            print('불가능합니다. 양의 정수를 다시 입력해주세요')
            continue

def judge_of_nonsingular(n): # 주어진 행렬이 non-singular인지 확인하는 함수.
    for i in range(n):
        globals()['b{}'.format(i)]=globals()['a{}'.format(i)][:] #객체호출의 특성을 지닌 파이썬이기 때문에 원래의 리스트 a를 b라는 새로운 리스트이름으로 복사
    make_upper_triangular_matrix(n,0) # triangular_matrix로 만든 후 determinant 구하는게 쉬우므로 이 함수 호출.
    determinant=1
    for i in range(n):
        determinant*=globals()['b{}'.format(i)][i] #어차피 triangular_matrix의 determinant가 0만 아니면 원래 행렬은 non-singular이다.
    if determinant!=0:
        print('This is non-singular matrix')
        return True
    else:
        print('This is singular matrix')
        return False

def get_and_show_augmented_matrix(n): #이제 AX=I의 형태로 만듦.[A:I]
    for i in range(0,n):
        globals()['I{}'.format(i)]=[] #먼저 In을 생성후 두 행렬 결합.
        for j in range(0,n):
            if i==j :
                globals()['I{}'.format(i)].append(1)
            else :
                globals()['I{}'.format(i)].append(0)
        globals()['augmented_matrix{}'.format(i)]=globals()['a{}'.format(i)]+globals()['I{}'.format(i)]
    print('augmented_matrix is')
    for i in range(0,n):
        globals()['augmented_matrix{}'.format(i)]
        print(globals()['augmented_matrix{}'.format(i)])

def make_upper_triangular_matrix(n,k): # k is a number of experiances this process. #A의 upper_triangular_matrix를 만들기 위한 함수.
    if k==n:
        print('upper_triangular_matrix_of_A is')
        for i in range(n):
            print(globals()['b{}'.format(i)])
        print('finish')
    else :
        arrangement_of_matrix(n,k)
        for i in range(k,n):
            first_element=globals()['b{}'.format(i)][k]
            for j in range(n):
                if first_element!=0:
                    element=globals()['b{}'.format(i)][j]
                    globals()['b{}'.format(i)][j]=Fraction(element,first_element) #각행을 제일 첫번째 엘리멘트로 나누는 작업. 0이 아닐때만.

        for i in range(k,n-1):
            if globals()['b{}'.format(i+1)][k]==1: #맨 앞 엘리멘트가 위 과정으로 인해 1아니면 0이므로 0일땐 빼면 안되니까 1일때만 작업.
                for j in range(n):
                    globals()['b{}'.format(i+1)][j]=globals()['b{}'.format(i+1)][j]-globals()['b{}'.format(k)][j]
                # k 번째 행의 맨앞 element를 1로 같은 열의 다른 element들은 모두 0으로 만들어주는 작업
        for i in range(n):
            print(globals()['b{}'.format(i)])
        make_upper_triangular_matrix(n,k+1) #k를 늘려가며 row ecelon form을 만들어 나간다.

def make_upper_triangular_augmented_matrix(n,k): # k is a number of experiances this process.
    if k==n:
        print('finish')
    else :
        arrangement_of_matrix2(n,k)
        for i in range(k,n):
            first_element=globals()['augmented_matrix{}'.format(i)][k]
            for j in range(2*n): #얘는 열의 개수가 두배이다.
                if first_element!=0:
                    element=globals()['augmented_matrix{}'.format(i)][j]
                    globals()['augmented_matrix{}'.format(i)][j]=Fraction(element,first_element) #각행을 제일 첫번째 엘리멘트로 나누는 작업
        for i in range(k,n-1):
            if globals()['augmented_matrix{}'.format(i+1)][k]==1:
                for j in range(2*n):
                    globals()['augmented_matrix{}'.format(i+1)][j]=globals()['augmented_matrix{}'.format(i+1)][j]-globals()['augmented_matrix{}'.format(k)][j]
                # row echelon form 을 만드는 과정.
        print('after the matrix is %dth row operated'%(k+1))
        for i in range(n):
            print(globals()['augmented_matrix{}'.format(i)])
        make_upper_triangular_augmented_matrix(n,k+1)

def make_lower_triangular_augmented_matrix(n,num_of_diagonal,k): #k는 위와 똑같고, num_of_diagonal은 대각선의 번호를 의미한다. 주대각선은 0이고 오른쪽 위 순서대로 1,2,3,... 이다.
    if k==n:
        print('finish')
    else:
        for i in range(k+1,n):
            element=globals()['augmented_matrix{}'.format(k)][i]
            for j in range(num_of_diagonal,2*n):
                if element!=0:
                    globals()['augmented_matrix{}'.format(k)][j]=globals()['augmented_matrix{}'.format(k)][j]-element*globals()['augmented_matrix{}'.format(i)][j]
        print('after the matrix is %d row operated'%(k+1))
        for i in range(n):
            print(globals()['augmented_matrix{}'.format(i)])
        make_lower_triangular_augmented_matrix(n,num_of_diagonal+1,k+1)

def arrangement_of_matrix(n,k): #처음 매트릭스를 upper_triangular_matrix를 만들 때 대각성분이 0인경우 0이아니게 만들어주는 작업
    if globals()['b{}'.format(k)][k]==0:
        for i in range(k,n):
            if globals()['b{}'.format(i)][k]!=0:
                for j in range(n):
                    globals()['b{}'.format(k)][j]+=globals()['b{}'.format(i)][j]
                break

def arrangement_of_matrix2(n,k): #얘는 augmented_matrix를 upper_triangular_matrix로 만들 때 정리작업.
    if globals()['augmented_matrix{}'.format(k)][k]==0:
        for i in range(k,n):
            if globals()['augmented_matrix{}'.format(i)][k]!=0:
                for j in range(2*n):
                    globals()['augmented_matrix{}'.format(k)][j]+=globals()['augmented_matrix{}'.format(i)][j]
                break

def get_inverse_matrix(n,k): #역행렬 보여주는 함수
    print('따라서 주어진 행렬')
    for i in range(n):
        print(globals()['a{}'.format(i)])
    print('의 역행렬은')
    for i in range(n):
        globals()['inverse_matrix{}'.format(i)]=globals()['augmented_matrix{}'.format(i)][n:2*n] #inverse_matrix를 따로 생성
        print(globals()['inverse_matrix{}'.format(i)])
    print('입니다.')

def multiply_of_two_matrix(n): #행렬 곱해서 단위행렬 나오는지 확인하는 함수
    for i in range(n): #두 매트릭스를 곱했을때 나오는 결과를 담을 빈 리스트를 만드는 작업
        globals()['multiple_matrix{}'.format(i)]=[]
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(n):
                sum+=globals()['a{}'.format(i)][k]*globals()['inverse_matrix{}'.format(k)][j]#i행을 j열에 곱한것을 sum에 저장
            globals()['multiple_matrix{}'.format(i)].append(sum)    #한개의 element씩 리스트에 추가.
    print('두 행렬의 곱은 아래와 같습니다.(AA-1형태)')
    for i in range(n): # 결과확인
        print(globals()['multiple_matrix{}'.format(i)])
    for i in range(n): #A-1A형태로 다시 확인
        globals()['multiple_matrix{}'.format(i)]=[]
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(n):
                sum+=globals()['inverse_matrix{}'.format(i)][k]*globals()['a{}'.format(k)][j]#i행을 j열에 곱한것을 sum에 저장
            globals()['multiple_matrix{}'.format(i)].append(sum)    #한개의 element씩 리스트에 추가.
    print('두 행렬의 곱은 아래와 같습니다.(A-1A형태)')
    for i in range(n): # 결과확인
        print(globals()['multiple_matrix{}'.format(i)])

def main():

    n=define_n()
    while 1:
        get_and_show_matrix(n)
        T_OR_F=judge_of_nonsingular(n)
        if T_OR_F==True:
            get_and_show_augmented_matrix(n)
            make_upper_triangular_augmented_matrix(n,0)
            make_lower_triangular_augmented_matrix(n,1,0)
            get_inverse_matrix(n,0)
            multiply_of_two_matrix(n)
            break
        else:
            print('역행렬이 존재하지 않는 행렬입니다. 프로그램을 종료합니다.')
            break








if __name__=='__main__':
    main()
