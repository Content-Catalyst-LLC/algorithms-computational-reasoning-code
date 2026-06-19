fn dependency_score(a:f64,v:f64,c:f64,s:f64,e:f64)->f64{100.0*(0.22*a+0.22*v+0.18*c+0.24*s+0.14*e)}
fn switching_cost(m:f64,r:f64,t:f64,d:f64,l:f64)->f64{m+r+t+d+l}
fn ratio(n:f64,d:f64)->f64{if d==0.0{0.0}else{n/d}}
fn main(){ println!("test_name,value\ndependency_score,{:.3}\nswitching_cost,{:.3}\napi_dependency_ratio,{:.6}\nvisibility_share,{:.6}",dependency_score(.80,.90,.70,.85,.65),switching_cost(45000.0,120000.0,18000.0,24000.0,75000.0),ratio(850000.0,1000000.0),ratio(250000.0,5000000.0)); }
