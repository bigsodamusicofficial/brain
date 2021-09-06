import markdown
import os
from datetime import date

today = date.today()

big_list = open("src/BIG_LIST.txt","a")

big_list.truncate(0)

print " --- FILE OPENED --- "

print(os.getcwd())

all_done_tasks = ""

with open("src/grep_out") as file_in:
  for file_to_open in file_in:
    f = file_to_open
    if ".DS_Store" in f or "tmp.drive" in f or "big_list" in f or "FINISHED" in f or "horizon" in f or "src" in f:
      continue
    if ".txt" in f and ".//" in f:
      print file_to_open[:-7]
    else:
      continue

    append_line = False
    first_task = True

    fresh_write = ""

    with open(file_to_open[:-7]) as read_file:
      for read in read_file:
        if read[:3] == " X " or read[:3] == " x ":
          all_done_tasks += (today.strftime("%Y.%m.%d") + ": " + file_to_open[3:-11] +"    " + read)
          continue
        else:
          fresh_write += read

        if "TO DO" in read:
          append_line = True
          continue
        if append_line and read == "\n":
          append_line = False
        if append_line:
          if first_task:
            big_list.write("\n")
            big_list.write(file_to_open[(1+file_to_open.rfind("/")):-11] + "\n")
          big_list.write(read)
          first_task = False

    big_list.write("\n")

    refresh_list = open(file_to_open[:-7],"w")
    refresh_list.write(fresh_write)
    refresh_list.close()

big_list.close()

done_tasks = open("_done_tasks","a")
done_tasks.write(all_done_tasks)
done_tasks.close()


big_fancy_string = ""

with open("src/BIG_LIST.txt") as list:
  for li in list:
    if li == "\n":
      big_fancy_string += "\n"
      continue
    if " - " in li:
      big_fancy_string += li
    else:
      big_fancy_string += "### "
      big_fancy_string += li
    big_fancy_string += "  "

md_convert = open("BIG_LIST.html","a")
md_convert.truncate(0)
md_convert.write(markdown.markdown(big_fancy_string.decode("ascii","ignore")))
md_convert.close()

print " --- FILE CLOSED --- "
