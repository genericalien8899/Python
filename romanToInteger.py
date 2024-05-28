s = "MCXXIV"
total = 0
for e, i in enumerate(s):
  if i == "I":
    if e < (len(s) - 1) and (s[e + 1] == "V" or s[e + 1] == "X"):
      total -= 1
    else:
      total += 1
  elif i == "X":
    if e < (len(s) - 1) and (s[e + 1] == "L" or s[e + 1] == "C"):
      total -= 10
    else:
      total += 10
  elif i == "C":
    if e < (len(s) - 1) and (s[e + 1] == "D" or s[e + 1] == "M"):
      total -= 100
    else:
      total += 100
    elif i == "V":
      total += 5
    elif i == "L":
      total += 50
    elif i == "D":
      total += 500
    elif i == "M":
     total += 1000
print(total)

#  Best java solution found in discussion

# public class JavaExample {
#     public static void main(String[] args) {
#         // Correcting the string literal by enclosing it in double quotes
#         String str = new String("MCMXCIV");

#         // Creating an instance of JavaExample to call the non-static method
#         JavaExample example = new JavaExample();
#         System.out.println(example.romanToInt(str));
#     }

#     public int romanToInt(String s) {
#         int answer = 0, number = 0, prev = 0;

#         for (int j = s.length() - 1; j >= 0; j--) {
#             switch (s.charAt(j)) {
#                 case 'M': number = 1000; break;
#                 case 'D': number = 500; break;
#                 case 'C': number = 100; break;
#                 case 'L': number = 50; break;
#                 case 'X': number = 10; break;
#                 case 'V': number = 5; break;
#                 case 'I': number = 1; break;
#             }
#             if (number < prev) {
#                 answer -= number;
#             } else {
#                 answer += number;
#             }
#             prev = number;
#         }
#         return answer;
#     }
# }
