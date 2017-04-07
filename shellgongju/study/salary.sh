read -p "Salary:" salary
read -p "Tax(0.xx):" tax
read -p "Working days:" day
read -p "time left from working day(hours):" leave
deduct=$(echo "scale=1;$salary/$day/8*$leave+$salary*$tax"|bc -l)
deduct=$(echo $deduct|awk -F\. '{print $1}') 
pay=$[$salary-$deduct]
echo pay=$pay


