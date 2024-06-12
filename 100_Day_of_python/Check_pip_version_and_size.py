import os
import pkg_resources

def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)  # Convert to MB

total_size = 0
dists = [d for d in pkg_resources.working_set]

for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        total_size += size
        print(f"{dist}: {size:.2f} MB")
        print("-" * 40)
    except OSError:
        print('{} no longer exists'.format(dist.project_name))

print(f"Total size: {total_size:.2f} MB")
# total of size : 


