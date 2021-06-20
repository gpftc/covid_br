import covidbr as cb

cb.logging.__log__ = True

log = cb.log

for i in range(1,100_000):
    log(f'time: {i}')
