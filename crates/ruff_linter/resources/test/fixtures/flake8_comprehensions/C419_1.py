sum([x.val for x in bar])
min([x.val for x in bar])
max([x.val for x in bar])
sum([x.val for x in bar], 0)

# Ok
sum(x.val for x in bar)
min(x.val for x in bar)
max(x.val for x in bar)
sum(x.val for x in bar, 0)
