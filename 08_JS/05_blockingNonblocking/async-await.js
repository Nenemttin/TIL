const getUser = id => {
    const users = [
        {id: 1, githubID: 'nenemttin'},
        {id: 2, githubID: 'gwaldo'},
    ];

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const user = users.find(user => user.id === id);
            user ? resolve(user) : reject(new Error(`Can't find user ${id}`));
            // if (user) {
            //     resolve(user)
            // } else {
            //     reject(new Error(`Cannot find user with id ${id}`))
            // }
        }, 2000)
    });
};

const getRepos = user => {
    const repos = [
        'TIL',
        'Workshop_HW',
        'Python',
        'JS'
    ];

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (repos) {
                resolve(repos);
            } else {
                reject(new Error(`Can't find ${user}'s repos`));
            }
        }, 2000)
    });

};

const getCommits = repo => {
    const commits = ['Init repo', 'Make index.html'];

    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (commits) {
                resolve(commits);
            } else {
                reject(new Error('ERROR!!!'));
            }
        }, 2000)
    });
};

async function main () {
    try {
        const user = await getUser(1);
        const repos = await getRepos(user);
        const commits = await getCommits(repos[0]);
        console.log(commits.length);
    } catch (e) {
        console.error(e);
    }
}

main();

