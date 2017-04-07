read -p "Salary:" salary
read -p "Tax:" tax
read -p "Working days:" day
read -p "time left from working day(hours):" leave
deduct=$(echo "scale=1;$salary/$day/8*$leave+$salary*$tax"|bc -l|cut -d . -f 1)
#deduct=$(echo $deduct|awk -F\. '{print $1}')  #awk method,also process the variable like string
pay=$[$salary-$deduct]
echo pay=$pay
