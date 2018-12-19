import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

def fireSever(url):
    try:
        contents = urllib.request.urlopen(url).getcode();
        return contents;
    except:
        return 666;

# initial
total_200 = 0;
total_666 = 0;
target_url = "http://www.reg.kmitl.ac.th/";
# total thread is thread_num*thread_loop
thread_num = 800;
thread_loop = 10;

# init list
url_list = [];
for i in range(thread_num):
    url_list.append(target_url);

for i in range(thread_loop):
    # task
    pool = ThreadPool(thread_num);
    results = pool.map(fireSever, url_list);
    pool.close();
    pool.join();
    # summary building
    total_200 += sum(1 for code in results if code == 200);
    total_666 += sum(1 for code in results if code == 666);

# summary
print("200: ", (total_200/(thread_num*thread_loop))*100,"%");
print("666: ", (total_666/(thread_num*thread_loop))*100,"%");
