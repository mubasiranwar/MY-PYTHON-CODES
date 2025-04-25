with(open("1.txt","w")) as f:#trucating the old writing
    f.write("Hi I am writing.")

with (open("1.txt","a")) as k:#it write but not truncate it write at end
    k.write("Than I Will focuse on it")
    
with (open("1.txt","w+")) as a:#use for writing and reading
    a.write("Than I Will go to oops.")
    print(a.read())