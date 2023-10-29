def TowerofHanoi(n: object, from_rod: object, to_rod: object, aux_rod: object) -> object:
    if n==1:
        print("move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerofHanoi(n-1,from_rod,aux_rod,to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerofHanoi(n-1,aux_rod,to_rod,from_rod)


n=int(input("enter the value of disk number:"))
TowerofHanoi( n, 'A', 'C', 'B')

