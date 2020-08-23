import pushbullet as p

a = p.Pushbullet("o.ESq4Rr87mDTDgKKnFjnxcKGwkj9gW8J2")
device = a.devices[0]
a.push_note("Visitors","Please attend our Visitors ")
a.push_sms(device,"8896575650","https://forms.gle/uXx9hsP7ykB9c7yF6")
# a.push_sms(device,"7652055328","Please contact on this number: 7007083654")
# a.push_list("User Details",gs.data)