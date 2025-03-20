// -*- encoding: utf-8 -*-*
// @Introduce  :
// @File       : minimumcost.rs
// @Author     : ryrl
// @Email      : ryrl970311@gmail.com
// @Time       : 2025/03/20 18:11
// @Description:

use crate::Solution;

pub trait MinimumCost {
    fn minimum_cost(
        n: usize,
        edges: &Vec<(usize, usize, i32)>,
        query: &Vec<(usize, usize)>,
    ) -> Vec<i32>;

    fn bfs_component(
        start: usize,
        components_id: usize,
        visited: &mut [bool],
        components: &mut [usize],
        adj: &Vec<Vec<(usize, i32)>>,
    ) -> i32;
}

impl MinimumCost for Solution {
    fn minimum_cost(
        n: usize,
        edges: &Vec<(usize, usize, i32)>,
        query: &Vec<(usize, usize)>,
    ) -> Vec<i32> {
        let mut adj = vec![Vec::new(); n];

        for &(src, dst, weight) in edges {
            adj[src].push((dst, weight));
            adj[dst].push((src, weight));
        }

        let mut visited = vec![false; n];
        let mut components = vec![0; n];
        let mut component_cost = Vec::new();
        let mut component_id = 0;

        for node in 0..n {
            if !visited[node] {
                let cost =
                    Self::bfs_component(node, component_id, &mut visited, &mut components, &adj);
                component_cost.push(cost);
                component_id += 1;
            }
        }

        let mut res = Vec::with_capacity(query.len());
        for &(src, dst) in query {
            if components[src] == components[dst] {
                res.push(component_cost[components[src]]);
            } else {
                res.push(-1);
            }
        }
        res
    }

    fn bfs_component(
        src: usize,
        components_id: usize,
        visited: &mut [bool],
        components: &mut [usize],
        adj: &Vec<Vec<(usize, i32)>>,
    ) -> i32 {
        let mut queue = std::collections::VecDeque::new();
        let mut component_cost = -1;

        visited[src] = true;
        components[src] = components_id;
        queue.push_back(src);

        while let Some(node) = queue.pop_front() {
            for &(neighbor, weight) in &adj[node] {
                component_cost &= weight;
                if !visited[neighbor] {
                    visited[neighbor] = true;
                    components[neighbor] = components_id;
                    queue.push_back(neighbor);
                }
            }
        }
        component_cost
    }
}
