type Profile = { p1: string; p2: string; u1: number; u2: number };
const profiles: Profile[] = [{p1:"cooperate",p2:"cooperate",u1:3,u2:3},{p1:"cooperate",p2:"defect",u1:0,u2:5},{p1:"defect",p2:"cooperate",u1:5,u2:0},{p1:"defect",p2:"defect",u1:1,u2:1}];
console.log(profiles.map(p => ({...p, welfare: p.u1 + p.u2})));
