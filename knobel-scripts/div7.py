[(a,a*7)for a in range(10234,14109)if[str(a*100007).count(c)for c in"012345678"]==[1]*9]
[(a,a*7)for a in range(10234,14109)if all([str(a*100007).count(c)for c in"0123456789"])]
[(a,a*7)for a in range(10234,14109)if not set("0123456789").difference(str(a*100007))]
[(a,a*7)for a in range(10234,14109)if all(i in str(a*100007)for i in"0123456789")]
[(a,a*7)for a in range(10234,14109)if''.join(sorted(str(a*100007)))=="0123456789"]
