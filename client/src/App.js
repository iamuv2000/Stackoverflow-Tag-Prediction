import React, {useState} from 'react';
import './App.css';

export default function App() {

	const [question, setQuestion] = useState('');
	const [tags, setTags] = useState([]);

	const fetchTags = async() => {
		console.log(question)
		let response = await fetch('/api/getRecommendedTags', {
			headers:{
				'content-type': 'application/json'
			},
			method: 'post',
			body: JSON.stringify({
				question
			})
		})

		response = await response.json();
		console.log(response)

		// SET TAGS
		setTags(response)

	}

	return (
		<div className="App">
			<header className="App-header">
				<img src="https://cdn.sstatic.net/Sites/stackoverflow/company/Img/logos/so/so-logo.svg?v=a010291124bf" className="stackoverflow_logo" alt="logo"/>
			</header>

			<p id="header__text">Enter the question you intend to post to Stackoverflow to <span>generate a list of apt tags for the question!</span></p>

			<textarea 
				placeholder="Enter question here..."
				className="question__input"
				onChange={e => setQuestion(e.target.value)}
			/>
			<br />
			<button 
				id="submit"
				onClick={fetchTags}
			>
				Get Tags!
			</button>

			{/* PREDICTED TAGS */}
			
			<div className="stackoverflow__tag__container">
			{
				tags.map((tag) => {
					return <PredictedTag 
					key= {tag}
					tag={tag}
				/>
				})
			}
			</div>
			
		</div>
	);
}

// PREDICTED TAG COMPONENT
const PredictedTag = ({tag}) => {
	return(
		<div className="stackoverflow__tag">
			{tag}
		</div>
	)
}